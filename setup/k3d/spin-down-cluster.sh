#!/bin/bash

current_cluster=$(kubectl config current-context)

read -p "???> Are you sure you want to delete $current_cluster K3d cluster? (y/N)" -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    k3d cluster delete xlrcluster
fi
