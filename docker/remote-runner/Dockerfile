FROM xebialabsunsupported/release-runner:25.3.0-beta.715

USER root

RUN apt update && apt install -y curl jq dos2unix

COPY spin-remote-runner.sh /spin-remote-runner.sh
RUN chmod +x /spin-remote-runner.sh

ENTRYPOINT ["/spin-remote-runner.sh"]
