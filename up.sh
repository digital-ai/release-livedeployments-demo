#!/bin/bash

parse_arguments() {
  local state="none"
  local current_flag=""
  while [[ $# -gt 0 ]]; do
    case $state in
      none)
        case $1 in
          --release-zip|--deploy-zip)
            current_flag="$1"
            state="read-value"
            ;;
          *)
            echo "Unknown option: $1"
            exit 1
            ;;
        esac
        ;;
      read-value)
        if [[ $1 != --* && -n $1 ]]; then
          case $current_flag in
            --release-zip)
              RELEASE_ZIP="$1"
              RELEASE_DOCKER_PATH="docker/xl-release-from-zip"
              ;;
            --deploy-zip)
              DEPLOY_ZIP="$1"
              DEPLOY_DOCKER_PATH="docker/xl-deploy-from-zip"
              ;;
          esac
          state="none"
        else
          echo "Error: $current_flag requires a value."
          exit 1
        fi
        ;;
    esac
    shift
  done

  # Final validation for missing value
  if [[ $state == "read-value" ]]; then
    echo "Error: $current_flag requires a value."
    exit 1
  fi
}

DEPLOY_ZIP=''
RELEASE_ZIP=''
DEPLOY_DOCKER_PATH='docker/xl-deploy'
RELEASE_DOCKER_PATH='docker/xl-release'

echo "Script for automatically setting up Live Deployments Demo"
echo "You can provide a zip file for Release and/or Deploy with the following options:"
echo "  --release-zip <path_to_release_zip>"
echo "  --deploy-zip <path_to_deploy_zip>"
echo "If you don't provide a zip, the docker-compose will use the default images."

parse_arguments "$@"

if [[ -n "$RELEASE_ZIP" ]]; then
  echo "Using Release zip: $RELEASE_ZIP"
  cp "$RELEASE_ZIP" "$RELEASE_DOCKER_PATH/xl-release-build.zip"
fi
if [[ -n "$DEPLOY_ZIP" ]]; then
  echo "Using Deploy zip: $DEPLOY_ZIP"
  cp "$DEPLOY_ZIP" "$DEPLOY_DOCKER_PATH/xl-deploy-build.zip"
fi

echo ""
echo ""
echo "Spinning up Release and Deploy in Docker"
export RELEASE_DOCKER_PATH=$RELEASE_DOCKER_PATH
export DEPLOY_DOCKER_PATH=$DEPLOY_DOCKER_PATH

docker compose -f docker-compose.yaml up -d --build || exit 1

echo "
Please wait for the Release and Deploy servers to start up.
Tip: the services are available when the setup-1 container is no longer running."

echo "
To install additional components like ArgoCD and Flux, see setup/README.md or use the interactive CLI:
$ ./cli setup"
