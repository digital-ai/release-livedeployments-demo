from typing import List

RELEASE_URL: str = "http://localhost:5516"
DEPLOY_URL: str = "http://localhost:4516"

BASIC_AUTH_USER: str = "admin"
BASIC_AUTH_PASSWORD: str = "admin"

DEFAULT_TIMEOUT: int = 300
POLL_INTERVAL: int = 5

RUNNING_SERVICES: List[str] = ["deploy", "release", "remote-runner", "container-registry"]

SETUP_SERVICE: str = "setup"

HTTP_TIMEOUT: int = 5

DEFAULT_DEPLOY_DOCKER_PATH: str = "docker/xl-deploy"
DEFAULT_RELEASE_DOCKER_PATH: str = "docker/xl-release"
