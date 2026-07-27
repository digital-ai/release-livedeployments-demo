import subprocess


def wait_for_app_condition(
    app_name: str, namespace: str, condition: str = "available", timeout: int = 180
) -> bool:
    result = subprocess.run(
        [
            "kubectl",
            "wait",
            f"--for=condition={condition}",
            app_name,
            "-n",
            namespace,
            f"--timeout={timeout}s",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0
