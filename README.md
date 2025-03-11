# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

## Perequisites

* Docker 
* `host.docker.internal` in `/etc/hosts` pointing to `127.0.0.1`
* create `secret.xlvals` file and fill in credentials, see `secret.xlvals.example`

## Start & stop

**Note:** The setup requires __docker, k3d, helm, git, kubectl, argocd, and flux__ to be installed on the host machine. Make sure you have GITHUB_TOKEN ready for the setup of FluxCD together with a clonable repository.

To start the entire demo, including setup:

    ./up.sh

**Note:** The setup will ask for prompts and will take a few minutes to complete.

**Slow installation:** 
* Part of installation process for building Release Runner image is to download the `golang:1.17` image. This image is around 1.5GB and might take a while to download.
* Part of installation for adding the `fluxcd` repository is slow because starting up of FluxCD controllers takes a while.

To tear down the entire demo:

    ./down.sh
