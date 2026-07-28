import subprocess
from typing import List


def _run_diagnostic_command(cmd: List[str]) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    output = (result.stdout or "") + (result.stderr or "")
    return f"$ {' '.join(cmd)}\n{output}"


def get_cluster_diagnostics() -> str:
    commands: List[List[str]] = [
        ["k3d", "cluster", "list"],
        ["kubectl", "get", "all", "-A", "-o", "wide"],
        ["kubectl", "get", "events", "-A", "--sort-by=.lastTimestamp"],
    ]
    return "\n\n".join(_run_diagnostic_command(cmd) for cmd in commands)


def wait_for_app_ready(
    resource: str,
    namespace: str,
    timeout: int = 180,
) -> bool:
    result = subprocess.run(
        [
            "kubectl",
            "rollout",
            "status",
            resource,
            "-n",
            namespace,
            f"--timeout={timeout}s",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def force_fluxcd_reconcile(
    kustomization: str = "podinfo", namespace: str = "podinfo", timeout: int = 60
) -> bool:
    result = subprocess.run(
        [
            "flux",
            "reconcile",
            "kustomization",
            kustomization,
            "-n",
            namespace,
            "--with-source",
            f"--timeout={timeout}s",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0
