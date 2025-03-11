#!/bin/bash

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

echo "Spinning up dockerized Release and Deploy"
docker compose -f docker-compose.yaml up -d --build

echo "Select where to run Release Runner:"
echo "1) Docker"
echo "2) Local K3d Cluster"
read -p "???> Enter your choice (1 or 2): " -n 1 -r
echo

if [[ $REPLY =~ ^[1]$ ]]; then
    echo "Spinning up dockerized Release Runner"
    docker compose -f docker-compose-runner.yaml up -d --build
    exit 0
else
    echo "Spinning up k3d cluster"
    $SCRIPT_DIR/k3d/spin-up-cluster.sh
fi


