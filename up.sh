#!/bin/bash

parse_arguments() {
  local state="none"
  local current_flag=""
  while [[ $# -gt 0 ]]; do
    case $state in
      none)
        case $1 in
          --release-zip|--deploy-zip|--runner-docker-image)
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
            --runner-docker-image)
              RUNNER_DOCKER_IMAGE="$1"
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

# Extract default runner image from Dockerfile so we don't hardcode it in multiple places
DEFAULT_RUNNER_IMAGE=$(grep "ARG RUNNER_DOCKER_IMAGE=" docker/remote-runner/Dockerfile | cut -d= -f2)
RUNNER_DOCKER_IMAGE=''

echo "Script for automatically setting up Live Deployments Demo"
echo "You can provide a zip file for Release and/or Deploy with the following options:"
echo "  --release-zip <path_to_release_zip>"
echo "  --deploy-zip <path_to_deploy_zip>"
echo "If you don't provide a zip, the docker-compose will use the default images."
echo ""
echo "You can also provide a custom Runner to use with the following option:"
echo "  --runner-docker-image <docker_image_name>"

parse_arguments "$@"

if [[ -n "$RELEASE_ZIP" ]]; then
  echo "Using Release zip: $RELEASE_ZIP"
  cp "$RELEASE_ZIP" "$RELEASE_DOCKER_PATH/xl-release-build.zip"
fi
if [[ -n "$DEPLOY_ZIP" ]]; then
  echo "Using Deploy zip: $DEPLOY_ZIP"
  cp "$DEPLOY_ZIP" "$DEPLOY_DOCKER_PATH/xl-deploy-build.zip"
fi
if [[ -n "$RUNNER_DOCKER_IMAGE" ]]; then
  echo "Using Runner Docker Image: $RUNNER_DOCKER_IMAGE"
else
  RUNNER_DOCKER_IMAGE=$DEFAULT_RUNNER_IMAGE
fi

echo ""
echo ""
echo "Spinning up dockerized Release and Deploy"
RELEASE_DOCKER_PATH=$RELEASE_DOCKER_PATH \
DEPLOY_DOCKER_PATH=$DEPLOY_DOCKER_PATH \
RUNNER_DOCKER_IMAGE=$RUNNER_DOCKER_IMAGE \
docker compose -f docker-compose.yaml up -d --build
echo "Please wait for the Release and Deploy to start up..."

echo "See setup/README.md to install additional components like ArgoCD and Flux."
echo "$ ./cli setup    # Interactive setup with Instacli: - https://github.com/Hes-Siemelink/instacli"
