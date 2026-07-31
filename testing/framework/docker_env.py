import json
import os
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, List

import requests

from . import config


class ServiceFailedError(Exception):
    """Raised when a service container has exited unexpectedly with a non-zero code."""

    def __init__(self, service: str, exit_code: int):
        self.service = service
        self.exit_code = exit_code
        message = (
            f"'{service}' service exited unexpectedly with code {exit_code}. "
            f"Check `docker compose logs {service}` for details."
        )
        super().__init__(message)


def _compose_file(repo_root: Path) -> str:
    return str(repo_root / "docker-compose.yaml")


def _compose_env() -> Dict[str, str]:
    """Set RELEASE_DOCKER_PATH/DEPLOY_DOCKER_PATH defaults (as up.sh does) to avoid compose warnings."""
    env = os.environ.copy()
    env.setdefault("RELEASE_DOCKER_PATH", config.DEFAULT_RELEASE_DOCKER_PATH)
    env.setdefault("DEPLOY_DOCKER_PATH", config.DEFAULT_DEPLOY_DOCKER_PATH)
    return env


def get_service_state(repo_root: Path, service: str) -> List[Dict[str, Any]]:
    result = subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            _compose_file(repo_root),
            "ps",
            "-a",
            "--format",
            "json",
            service,
        ],
        capture_output=True,
        text=True,
        check=False,
        env=_compose_env(),
    )

    output = result.stdout.strip()
    if not output:
        return []

    entries: List[Dict[str, Any]] = []
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        parsed = json.loads(line)
        if isinstance(parsed, list):
            entries.extend(parsed)
        else:
            entries.append(parsed)
    return entries


def _exit_code_of(entry: Dict[str, Any]) -> int:
    exit_code = entry.get("ExitCode", 1)
    try:
        return int(exit_code)
    except (TypeError, ValueError):
        return 1


def check_running_services(repo_root: Path, services: List[str]) -> Dict[str, bool]:
    status: Dict[str, bool] = {}
    for service in services:
        entries = get_service_state(repo_root, service)
        is_running = False
        for entry in entries:
            state = entry.get("State", "").lower()
            if state == "running":
                is_running = True
                break
            if state == "exited":
                exit_code = _exit_code_of(entry)
                if exit_code != 0:
                    raise ServiceFailedError(service, exit_code)
        status[service] = is_running
    return status


def check_setup_service(repo_root: Path, service: str = config.SETUP_SERVICE) -> bool:
    entries = get_service_state(repo_root, service)
    if not entries:
        return False

    entry = entries[0]
    state = entry.get("State", "").lower()

    if state == "running":
        return False

    if state == "exited":
        exit_code = _exit_code_of(entry)
        if exit_code == 0:
            return True
        raise ServiceFailedError(service, exit_code)

    return False


def check_http_ready(url: str, timeout: int = config.HTTP_TIMEOUT) -> bool:
    try:
        response = requests.get(
            url,
            auth=(config.BASIC_AUTH_USER, config.BASIC_AUTH_PASSWORD),
            timeout=timeout,
        )
        return 200 <= response.status_code < 400
    except requests.exceptions.RequestException:
        return False


def get_all_container_statuses(repo_root: Path) -> str:
    sections: List[str] = []

    compose_ps = subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            _compose_file(repo_root),
            "ps",
            "-a",
        ],
        capture_output=True,
        text=True,
        check=False,
        env=_compose_env(),
    )
    sections.append("$ docker compose ps -a\n" + compose_ps.stdout + compose_ps.stderr)

    all_containers = subprocess.run(
        [
            "docker",
            "ps",
            "-a",
            "--format",
            "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    sections.append("$ docker ps -a\n" + all_containers.stdout + all_containers.stderr)

    return "\n".join(sections)


def get_service_logs(repo_root: Path, service: str, tail: int = 50) -> str:
    result = subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            _compose_file(repo_root),
            "logs",
            "--tail",
            str(tail),
            service,
        ],
        capture_output=True,
        text=True,
        check=False,
        env=_compose_env(),
    )
    return result.stdout + result.stderr


def dump_relevant_container_logs(output_dir: Path) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    names_result = subprocess.run(
        [
            "docker",
            "ps",
            "-a",
            "--filter",
            "network=demo-network",
            "--format",
            "{{.Names}}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    relevant_names = []
    for name in names_result.stdout.splitlines():
        if name and not name.startswith("k3d-"):
            relevant_names.append(name)

    written_files: List[Path] = []
    for name in relevant_names:
        logs_result = subprocess.run(
            ["docker", "logs", "--timestamps", name],
            capture_output=True,
            text=True,
            check=False,
        )
        log_file = output_dir / f"{name}.log"
        log_file.write_text(logs_result.stdout + logs_result.stderr)
        written_files.append(log_file)

    return written_files


def wait_for_stack_ready(
    repo_root: Path,
    timeout: int = config.DEFAULT_TIMEOUT,
    poll_interval: int = config.POLL_INTERVAL,
    release_url: str = config.RELEASE_URL,
    deploy_url: str = config.DEPLOY_URL,
) -> None:
    deadline = time.monotonic() + timeout
    last_status: Dict[str, Any] = {}

    while time.monotonic() < deadline:
        running_status = check_running_services(repo_root, config.RUNNING_SERVICES)
        setup_done = check_setup_service(repo_root)

        last_status = dict(running_status)
        last_status["setup_done"] = setup_done

        all_running = True
        for is_running in running_status.values():
            if not is_running:
                all_running = False
                break

        if all_running and setup_done:
            release_ready = check_http_ready(release_url)
            deploy_ready = check_http_ready(deploy_url)
            last_status["release_http"] = release_ready
            last_status["deploy_http"] = deploy_ready
            if release_ready and deploy_ready:
                return

        time.sleep(poll_interval)

    raise TimeoutError(
        f"Stack did not become ready within {timeout}s. Last known status: {last_status}"
    )
