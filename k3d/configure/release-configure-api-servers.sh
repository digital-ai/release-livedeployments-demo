#!/bin/bash



#!/bin/bash


read -p "???> Do you want to add configuration for ArgoCD Server and FluxCD Server in Release? (Y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]; then
    exit 0
fi
argoCdServerUrl=https://argocd-server.argocd
argoCdUsername=admin
argoCdPassword=password

fluxCdServerUrl=https://kubernetes.default.svc
clientCrt=`kubectl config view --raw -o jsonpath='{.users[?(@.name=="admin@k3d-xlrcluster")].user.client-certificate-data}'`
clientKey=`kubectl config view --raw -o jsonpath='{.users[?(@.name=="admin@k3d-xlrcluster")].user.client-key-data}'`

# Prepare the secrets.xlvals file
cat <<EOF > config-scenario/secrets.xlvals
# Connection details for the ArgoCD and Deploy services

argoCdServerUrl: $argoCdServerUrl
argoCdUsername: $argoCdUsername
argoCdPassword: $argoCdPassword

fluxCdServerUrl: $fluxCdServerUrl
fluxCdClientCrt: $clientCrt
fluxCdClientKey: $clientKey
EOF

docker compose -f docker-compose-config.yaml up --build

echo ":::> Added configuration for ArgoCD Server in Release"


