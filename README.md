# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

⚠️** Currently broken **⚠️

* Docker setup pulls nightly build of Digital.ai Release, but the bundled version of the `release-deploy-integration` plugin is not compatible with the Live Deployments feature.
* To resolve this problem, make sure nightly build bundles latest version of the plugin.

## Perequisites

* Docker 

## Start & stop

To start the entire demo, including setup:

    ./up.sh

To tear down the entire demo:

    ./down.sh
