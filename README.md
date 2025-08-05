# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

## Prerequisites

* Docker
* `host.docker.internal` in `/etc/hosts` pointing to `127.0.0.1`
* `host.k3d.internal` in `/etc/hosts` pointing to `127.0.0.1`
* Ports `4516`, `5516` and `5050` to be free on the host machine

## Start & stop

To start the entire demo, including setup:

    ./up.sh

To tear down the entire demo:

    ./down.sh

## Using release and deploy from zip

You can use custom versions of Release and Deploy by providing arguments to the `up.sh` script. For example:

```
--release-zip <path_to_release_zip>
--deploy-zip <path_to_deploy_zip>
```

Note: don't forget to add license files to the `xl-deploy-from-zip` and `xl-release-from-zip` folders in the `docker` directory.

## Using custom versions of Release, Deploy and Release Runner

You can manually configure which versions of Release, Deploy and Release Runner to use by editing the `Dockerfile` files of the corresponding services in the
`docker` directory. Simply change the `FROM` line to point to the desired version of the service.

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