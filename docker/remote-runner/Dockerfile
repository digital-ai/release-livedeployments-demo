ARG RUNNER_DOCKER_IMAGE="xebialabsunsupported/release-runner:25.3.0-beta.715"

FROM ${RUNNER_DOCKER_IMAGE}

USER root

RUN apt update && apt install -y curl jq dos2unix

COPY spin-remote-runner.sh /spin-remote-runner.sh
RUN chmod +x /spin-remote-runner.sh

ENTRYPOINT ["/spin-remote-runner.sh"]
