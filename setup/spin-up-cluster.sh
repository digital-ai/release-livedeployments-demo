#!/bin/bash

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
$SCRIPT_DIR/cluster/run-k3d.sh
$SCRIPT_DIR/release-runner/spin-up-k3d-runner.sh
$SCRIPT_DIR/cluster/populate-xlr-registry.sh
$SCRIPT_DIR/argo-cd/spin-up-k3d-argocd.sh
$SCRIPT_DIR/flux-cd/spin-up-k3d-fluxcd.sh
$SCRIPT_DIR/flux-cd/use-fluxcd-github-repo.sh
$SCRIPT_DIR/configure/release-configure-api-servers.sh
