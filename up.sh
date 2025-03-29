#!/bin/bash

echo "Spinning up dockerized Release and Deploy"
docker compose -f docker-compose.yaml up -d --build

echo "Spinning up dockerized Release Runner"
docker compose -f docker-compose-runner.yaml up -d --build

echo "See setup/README.md to install additional components like ArgoCD and Flux."
echo "$ cli setup    # Interactive setup with Instacli: - https://github.com/Hes-Siemelink/instacli"
