# Digital.ai live deployments demo repository

This repository contains demo for Digital.ai Release and Deploy live deployments.

## Perequisites

* Docker 
* `host.docker.internal` in `/etc/hosts` pointing to `127.0.0.1`

## After Release and Deploy are started

**IMPORTANT:** After Release and Deploy are started, you need to sync the Deploy event source with the Deploy server.
1. Navigate to Release
2. Navigate to folder `Application Demo`
3. Navigate to `Connections`
4. Edit `Deploy Status Webhook Event Source` event source
5. Click `Sync` in the top toolbar

## Start & stop

To start the entire demo, including setup:

    ./up.sh

To tear down the entire demo:

    ./down.sh
