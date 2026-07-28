#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from framework import config, docker_env
from framework.kubernetes_util import (
    force_fluxcd_reconcile,
    get_cluster_diagnostics,
    wait_for_app_ready,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTING_DIR = Path(__file__).resolve().parent
DOCKER_LOGS_DIR = TESTING_DIR / "test-results" / "docker-logs"
PYTEST_PHASE_ONE_COMMAND = [
    sys.executable,
    "-m",
    "pytest",
    "-m",
    "phase_one",
    "ui/tests",
]
PYTEST_PHASE_TWO_COMMAND = [
    sys.executable,
    "-m",
    "pytest",
    "-m",
    "phase_two",
    "ui/tests",
]


class PhaseFailedError(Exception):
    """Raised by a phase function to signal failure to main()."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run/validate the Release Live Deployments demo stack.",
    )
    parser.add_argument(
        "--release-zip", help="Path to a Release zip, passed through to up.sh"
    )
    parser.add_argument(
        "--deploy-zip", help="Path to a Deploy zip, passed through to up.sh"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=config.DEFAULT_TIMEOUT,
        help=f"Readiness timeout in seconds (default: {config.DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "--with-ui",
        action="store_true",
        help="Also run the Playwright pytest UI tests after readiness checks pass.",
    )
    parser.add_argument(
        "--down",
        action="store_true",
        help="Tear down the environment via down.sh at the end.",
    )
    parser.add_argument(
        "--cli-setup",
        action="store_true",
        help="Enables setup and testing of `./cli setup` script.",
    )
    parser.add_argument(
        "--skip-up",
        action="store_true",
        help="Skip calling up.sh (useful if the stack is already running).",
    )
    return parser.parse_args()


def log_banner(title: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n", flush=True)


def run_streaming(cmd: List[str], cwd: Optional[Path] = None) -> int:
    print(f"$ {' '.join(cmd)}", flush=True)
    process = subprocess.run(cmd, cwd=cwd)
    return process.returncode


def phase_up(release_zip: Optional[str], deploy_zip: Optional[str]) -> None:
    cmd = ["bash", "./up.sh"]
    if release_zip:
        cmd += ["--release-zip", release_zip]
    if deploy_zip:
        cmd += ["--deploy-zip", deploy_zip]

    exit_code = run_streaming(cmd, cwd=REPO_ROOT)
    if exit_code != 0:
        raise PhaseFailedError(f"up.sh failed with exit code {exit_code}.")


def phase_readiness(timeout: int) -> None:
    try:
        docker_env.wait_for_stack_ready(
            REPO_ROOT,
            timeout=timeout,
            poll_interval=config.POLL_INTERVAL,
        )
        print("Stack is ready: all services running and Release/Deploy responding.")
    except docker_env.ServiceFailedError as exc:
        _print_service_logs(exc.service)
        _dump_docker_logs()
        raise PhaseFailedError(str(exc)) from exc
    except TimeoutError as exc:
        _print_service_logs(config.SETUP_SERVICE)
        _dump_docker_logs()
        raise PhaseFailedError(f"Timed out waiting for stack readiness: {exc}") from exc


def _print_service_logs(service: str) -> None:
    print(f"\n--- Last 50 lines of '{service}' service logs ---", file=sys.stderr)
    try:
        logs = docker_env.get_service_logs(REPO_ROOT, service, tail=50)
        print(logs, file=sys.stderr)
    except Exception as exc:
        print(f"(failed to fetch {service} logs: {exc})", file=sys.stderr)
    print("--- end of logs ---\n", file=sys.stderr)


def _print_docker_diagnostics() -> None:
    print("\n--- Docker container statuses ---", file=sys.stderr)
    try:
        print(docker_env.get_all_container_statuses(REPO_ROOT), file=sys.stderr)
    except Exception as exc:
        print(f"(failed to fetch docker container statuses: {exc})", file=sys.stderr)
    print("--- end of docker container statuses ---\n", file=sys.stderr)


def _print_cluster_diagnostics() -> None:
    print("\n--- Kubernetes cluster state ---", file=sys.stderr)
    try:
        print(get_cluster_diagnostics(), file=sys.stderr)
    except Exception as exc:
        print(f"(failed to fetch cluster diagnostics: {exc})", file=sys.stderr)
    print("--- end of Kubernetes cluster state ---\n", file=sys.stderr)


def _dump_docker_logs() -> None:
    print(
        f"\n--- Dumping relevant docker container logs to {DOCKER_LOGS_DIR} ---",
        file=sys.stderr,
    )
    try:
        written_files = docker_env.dump_relevant_container_logs(DOCKER_LOGS_DIR)
        for log_file in written_files:
            print(f"  wrote {log_file}", file=sys.stderr)
    except Exception as exc:
        print(f"(failed to dump docker container logs: {exc})", file=sys.stderr)
    print("--- end of docker container logs dump ---\n", file=sys.stderr)


def __ui_tests(test_command: List[str]) -> None:
    env = os.environ.copy()
    env.setdefault("RELEASE_URL", config.RELEASE_URL)
    env.setdefault("DEPLOY_URL", config.DEPLOY_URL)

    cmd = test_command
    print(f"$ {' '.join(cmd)}", flush=True)
    process = subprocess.run(cmd, cwd=TESTING_DIR, env=env)
    if process.returncode != 0:
        raise PhaseFailedError(f"UI tests failed with exit code {process.returncode}.")


def phase_one_ui_tests() -> None:
    try:
        __ui_tests(PYTEST_PHASE_ONE_COMMAND)
    except PhaseFailedError:
        _print_docker_diagnostics()
        _dump_docker_logs()
        raise


def phase_two_ui_tests() -> None:
    try:
        __ui_tests(PYTEST_PHASE_TWO_COMMAND)
    except PhaseFailedError:
        _print_docker_diagnostics()
        _print_cluster_diagnostics()
        _dump_docker_logs()
        raise


def phase_cli_setup() -> None:
    cmd = ["bash", "./cli", "-q", "setup", "quickstart"]

    exit_code = run_streaming(cmd, cwd=REPO_ROOT)
    if exit_code != 0:
        _print_cluster_diagnostics()
        _dump_docker_logs()
        raise PhaseFailedError(f"cli setup failed with exit code {exit_code}.")


# cli setup does not wait for apps to become ready, for testing we need to wait for apps so that deployments are created
def wait_for_apps_ready() -> None:
    argo_result = wait_for_app_ready(
        resource="deployment/kustomize-guestbook-ui", namespace="guestbook"
    )
    flux_result = wait_for_app_ready(resource="deployment/podinfo", namespace="podinfo")
    if not argo_result or not flux_result:
        _print_cluster_diagnostics()
        _dump_docker_logs()
        raise PhaseFailedError(
            f"demo apps are not available in cluster. ArgoCD: {argo_result}, FluxCD: {flux_result}"
        )


def phase_cli_delete() -> None:
    cmd = ["bash", "./cli", "-q", "setup", "k3d", "delete"]

    exit_code = run_streaming(cmd, cwd=REPO_ROOT)
    if exit_code != 0:
        raise PhaseFailedError(f"cli setup failed with exit code {exit_code}.")


def phase_down() -> None:
    exit_code = run_streaming(["bash", "./down.sh"], cwd=REPO_ROOT)
    if exit_code != 0:
        raise PhaseFailedError(f"down.sh failed with exit code {exit_code}.")


def main() -> None:
    args = parse_args()
    exit_code = 0

    try:
        log_banner("Phase: Startup (up.sh)")
        if args.skip_up:
            print("--skip-up given, skipping stack startup.")
        else:
            phase_up(args.release_zip, args.deploy_zip)

        log_banner("Phase: Readiness checks")
        phase_readiness(args.timeout)

        log_banner("Phase: UI tests 1")
        if args.with_ui:
            phase_one_ui_tests()
        else:
            print(
                "Skipping UI tests (default). To run them manually later:\n"
                f"  cd {TESTING_DIR}\n"
                f"  {' '.join(PYTEST_PHASE_ONE_COMMAND)}\n"
            )

        log_banner("Phase: cli-setup cluster setup")
        if args.cli_setup:
            phase_cli_setup()
            log_banner("Waiting for apps to become ready")
            wait_for_apps_ready()
        else:
            print("--cli-setup not given, skipping cluster setup.")

        log_banner("Phase: UI tests 2")
        if args.cli_setup and args.with_ui:
            phase_two_ui_tests()
        else:
            print(
                "Skipping UI tests (default). To run them manually later:\n"
                f"  cd {TESTING_DIR}\n"
                f"  {' '.join(PYTEST_PHASE_TWO_COMMAND)}\n"
            )

    except PhaseFailedError as exc:
        print(f"\n{exc}", file=sys.stderr)
        exit_code = 1
    finally:
        log_banner("Phase: Teardown")
        if args.down:
            try:
                if args.cli_setup:
                    phase_cli_delete()
                phase_down()
            except PhaseFailedError as exc:
                print(f"\n{exc}", file=sys.stderr)
                exit_code = 1
        else:
            print("--down not given, leaving stack running.")

    if exit_code == 0:
        log_banner("Done")
        print("All requested phases completed successfully.")
    else:
        log_banner("Done (with failures)")
        print(
            "One or more phases failed. See output above for details.", file=sys.stderr
        )

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
