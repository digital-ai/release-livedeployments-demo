# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

## Perequisites

* Docker
* `host.docker.internal` in `/etc/hosts` pointing to `127.0.0.1`
* `host.k3d.internal` in `/etc/hosts` pointing to `127.0.0.1`
* create `secret.xlvals` file and fill in credentials, see `secret.xlvals.example`

## Start & stop

To start the entire demo, including setup:

    ./up.sh

To tear down the entire demo:

    ./down.sh

## Setting up Live Deployments manually

If you want to set up the live deployments manually, follow these steps:

* Make sure that you have necessary connections.
* Select a folder you want to create live deployments in.
* Open `Live Deployments` in Digital.ai Release and click connect
* Select the corresponding workflow and click `Run workflow`
* Select server connection and follow automated steps to set up the live deployments.

## Additional components

Use the interactive setup to install __k3d, argocd, and flux__  on the host machine. Make sure you have GITHUB_TOKEN ready for the setup of FluxCD together with
a clonable repository.

See [setup](setup/README.md) for more information on how to set up the demo environment.