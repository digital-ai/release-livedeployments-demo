# Digital.ai Release "Live Deployments" demo repository

This repository contains demo material for the Live Deployments feature of Digital.ai Release.

## Launching the demo 

### Prerequisites

* Docker
* `host.docker.internal` in `/etc/hosts` pointing to `127.0.0.1`
* `host.k3d.internal` in `/etc/hosts` pointing to `127.0.0.1`
* Ports `4516`, `5516` and `5050` to be free on the host machine

### Quick start & stop

To start the Docker demo environment with Release and Deploy:

    ./up.sh

This will produce a working Live Deployments demo based on Release and Deploy.
Additional components such as k3d, argocd, and flux will need to be installed separately, see below.

To tear down the entire demo:

    ./down.sh

## Demo flow

Navigate to **Folders** > **Application Demo**

> [!NOTE]
> If the **Application Demo** folder is not present, restart the `setup-1` container and check for errors in the log 

There should be a release called **Deploy Acme-Backend 1.0** that is running or completed.

> [!NOTE]
> If the release is in failed state, it may be that the task failed because the Deploy server was not properly initialized yet. Open the release and select **Retry** on the **Deploy to DEV** task to run it again. 

Go to the **Live Deployments** tab in the **Application Demo** folder. You should see the live deployments for the Acme-Backend application coming from Deploy

### Install additional components

You can install **k3d**, **ArgoCD**, and **Flux CD** locally on the host machine and integrate them those components into the demo environment running in Release. 

Start the interactive setup with the following command (unix only)

    ./cli setup

See [setup](setup/README.md) for more detailed description on how to set up the demo environment.

> [!NOTE]
> For Flux CD you will need a GitHub account and a GITHUB_TOKEN.


## Setting up Live Deployments manually

If you want to set up the live deployments manually, follow these steps:

* Make sure that you have necessary connections.
* Select a folder you want to create live deployments in.
* Open `Live Deployments` in Digital.ai Release and click connect
* Select the corresponding workflow and click `Run workflow`
* Select server connection and follow automated steps to set up the live deployments.

## Using custom versions of Release, Deploy and Release Runner

## Using different Docker images

You can manually configure which versions of Release, Deploy and Release Runner to use by editing the `Dockerfile` files of the corresponding services in the
`docker` directory. Simply change the `FROM` line to point to the desired version of the service.

### Using Release and Deploy from zip

You can use custom versions of Release and Deploy by providing arguments to the `up.sh` script. For example:

```
--release-zip <path_to_release_zip>
--deploy-zip <path_to_deploy_zip>
```

Note: don't forget to add license files to the `xl-deploy-from-zip` and `xl-release-from-zip` folders in the `docker` directory.

