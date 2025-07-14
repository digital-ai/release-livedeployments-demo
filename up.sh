#!/bin/bash

echo "Spinning up dockerized Release and Deploy"
docker compose -f docker-compose.yaml up -d --build
echo "Please wait for the Release and Deploy to start up..."

echo "See setup/README.md to install additional components like ArgoCD and Flux."
echo "$ ./cli setup    # Interactive setup with Instacli: - https://github.com/Hes-Siemelink/instacli"
