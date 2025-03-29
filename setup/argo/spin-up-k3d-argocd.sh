#!/bin/bash

current_cluster=$(kubectl config current-context)

read -p "???> Do you want to spin up ArgoCD on your cluster (current cluster context is $current_cluster)? (Y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]; then
    exit 0
fi

echo ":::> Spinning up ArgoCD on cluster..."
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl -n argocd patch secret argocd-secret \
  -p '{"stringData": {
    "admin.password": "$2a$10$rRyBsGSHK6.uc8fntPwVIuLVHgsAhAX7TcdrqW/RADU0uh7CaChLa",
    "admin.passwordMtime": "'$(date +%FT%T%Z)'"
  }}'

echo
if [ $? -eq 0 ]; then
    echo ":::> ArgoCD password is: password"
fi
echo
