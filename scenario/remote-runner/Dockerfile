FROM xebialabsunsupported/release-runner:24.1.2-rc.1

USER root

RUN apt update && apt install -y curl jq dos2unix

COPY spin-remote-runner.sh /spin-remote-runner.sh
RUN chmod +x /spin-remote-runner.sh

ENTRYPOINT ["/spin-remote-runner.sh"]
