# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

## Perequisites

* Docker 
* `host.docker.internal` in `/etc/hosts` pointing to `127.0.0.1`

<!-- For ArgoCD:
* create `secret.xlvals` file and fill in credentials, see `secret.xlvals.example`
-->

## Start & stop

To start the entire demo, including setup:

    ./up.sh

To tear down the entire demo:

    ./down.sh

