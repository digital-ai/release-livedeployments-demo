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
> If the release is in failed state, it may be that the task failed because the Deploy server was not properly initialized yet. Open the release and select *
*Retry** on the **Deploy to DEV** task to run it again.

Go to the **Live Deployments** tab in the **Application Demo** folder. You should see the live deployments for the Acme-Backend application coming from Deploy

### Install additional components

You can install **k3d**, **ArgoCD**, and **Flux CD** locally on the host machine and integrate them those components into the demo environment running in
Release.

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

**Note**: don't forget to add license files to the `xl-deploy-from-zip` and `xl-release-from-zip` folders in the `docker` directory.
Also, running from zip will most likely not include default plugins, which are only available in distribution packages.
You can install plugins manually, keep in mind that setup container will fail and will need to be ran again which can be done with this command 
```
docker container start release-livedeployments-demo-setup-1
```
Or run `demo-scenario/setup.yaml` and `demo-scenario/setup-live-deployment.yaml` files manually using `xl apply` command.

## Running Release Runner in kubernetes

To start runner in kubernetes you will need to have a values file

```
release:
  url: "http://release:5516"
  registrationToken: rpa_your_token_here
replicaCount: 1
resources:
  limits:
    cpu: 3
image:
  pullPolicy: Always
  registry: docker.io
  repository: xebialabsunsupported
  name: release-runner
  tag: 25.3.0-beta.715
```

Change tag version to desired one and don't forget to generate a registration token in Release and put it into the `registrationToken` field.

After creating values file run these commands to start the runner in kubernetes:

```
git clone git@github.com:digital-ai/release-runner-helm-chart.git
cd release-runner-helm-chart
helm repo add bitnami-repo https://charts.bitnami.com/bitnami
helm dependency update .
helm install release-runner . -n runner --create-namespace --values values.yaml
```

You can uninstall the runner with the following command:

```
helm uninstall release-runner -n runner
```