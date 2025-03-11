#!/bin/bash

read -p "???> Do you want to spin up xlrcluster with a registry on your local machine? (Y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]; then
    exit 0
fi

echo ":::> Spinning up k3d cluster"

if ! command -v k3d &> /dev/null
then
    echo "!!!>  could not be found"
    read -p "???> Do you want to install k3d using brew? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        brew install k3d
    else
        exit 1
    fi
fi

k3d cluster create xlrcluster --registry-create xlr-registry:5050
echo
echo ":::> Cluster xlrcluster created with registry xlr-registry:5050"
echo
