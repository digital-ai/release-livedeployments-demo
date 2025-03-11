#!/bin/bash

current_cluster=$(kubectl config current-context)

read -p "???> Do you want to spin up FluxCD on your cluster (current cluster context is $current_cluster)? (Y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]; then
    exit 0
fi

echo ":::> Spinning up FluxCD in $current_cluster"
kubectl apply -f https://github.com/fluxcd/flux2/releases/latest/download/install.yaml
echo ":::> FluxCD is ready..."
echo

