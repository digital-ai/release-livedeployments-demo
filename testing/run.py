#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from framework import config, docker_env

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTING_DIR = Path(__file__).resolve().parent


class PhaseFailedError(Exception):
    """Raised by a phase function to signal failure to main()."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run/validate the Release Live Deployments demo stack.",
    )
    parser.add_argument("--release-zip", help="Path to a Release zip, passed through to up.sh")
    parser.add_argument("--deploy-zip", help="Path to a Deploy zip, passed through to up.sh")
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
    log_banner("Phase: Startup (up.sh)")

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
        raise PhaseFailedError(str(exc)) from exc
    except TimeoutError as exc:
        _print_service_logs(config.SETUP_SERVICE)
        raise PhaseFailedError(f"Timed out waiting for stack readiness: {exc}") from exc


def _print_service_logs(service: str) -> None:
    print(f"\n--- Last 50 lines of '{service}' service logs ---", file=sys.stderr)
    try:
        logs = docker_env.get_service_logs(REPO_ROOT, service, tail=50)
        print(logs, file=sys.stderr)
    except Exception as exc:  # noqa: BLE001
        print(f"(failed to fetch {service} logs: {exc})", file=sys.stderr)
    print("--- end of logs ---\n", file=sys.stderr)


def phase_ui_tests() -> None:
    env = os.environ.copy()
    env.setdefault("RELEASE_URL", config.RELEASE_URL)
    env.setdefault("DEPLOY_URL", config.DEPLOY_URL)

    cmd = [sys.executable, "-m", "pytest", "ui/tests"]
    print(f"$ {' '.join(cmd)}", flush=True)
    process = subprocess.run(cmd, cwd=TESTING_DIR, env=env)
    if process.returncode != 0:
        raise PhaseFailedError(f"UI tests failed with exit code {process.returncode}.")


def phase_down() -> None:
    log_banner("Phase: Teardown (down.sh)")

    exit_code = run_streaming(["bash", "./down.sh"], cwd=REPO_ROOT)
    if exit_code != 0:
        raise PhaseFailedError(f"down.sh failed with exit code {exit_code}.")


def main() -> None:
    args = parse_args()
    exit_code = 0

    try:
        if args.skip_up:
            log_banner("Phase: Startup (up.sh)")
            print("--skip-up given, skipping stack startup.")
        else:
            phase_up(args.release_zip, args.deploy_zip)

        log_banner("Phase: Readiness checks")
        phase_readiness(args.timeout)

        log_banner("Phase: UI tests")
        if args.with_ui:
            phase_ui_tests()
        else:
            print(
                "Skipping UI tests (default). To run them manually later:\n"
                f"  cd {TESTING_DIR}\n"
                "  python -m pytest ui/tests\n"
            )
    except PhaseFailedError as exc:
        print(f"\n{exc}", file=sys.stderr)
        exit_code = 1
    finally:
        if args.down:
            try:
                phase_down()
            except PhaseFailedError as exc:
                print(f"\n{exc}", file=sys.stderr)
                exit_code = 1
        else:
            log_banner("Phase: Teardown (down.sh)")
            print("--down not given, leaving stack running.")

    if exit_code == 0:
        log_banner("Done")
        print("All requested phases completed successfully.")
    else:
        log_banner("Done (with failures)")
        print("One or more phases failed. See output above for details.", file=sys.stderr)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
