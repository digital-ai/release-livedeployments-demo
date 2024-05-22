# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

## Perequisites

* Docker
* Release license. Store it in  [docker/xl-release-from-zip/xl-release-license.lic](docker/xl-release-from-zip/xl-release-license.lic)
* Pre-built xl-release zip from branch. Ask Mario team. Put this zip file in [docker/xl-release-from-zip](docker/xl-release-from-zip). 

## Start & stop

To start the entire demo, including setup:

    ./up.sh

To tear down the entire demo:

    ./down.sh
