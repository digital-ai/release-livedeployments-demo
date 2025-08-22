# Install ArgoCD

Installs Argo CD in local k3d cluster

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

## Create namespace

Use `kubectl` to create the `argocd` namespace in the k3d cluster. This is where ArgoCD will be installed.

```shell
kubectl create namespace argocd
```

## Install ArgoCD using kubectl

Use `kubectl` to install ArgoCD in the `argocd` namespace and create a service account for it.

> Spinning up ArgoCD on K3d cluster

```shell show_output=false
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

> Waiting for ArgoCD server

Wait for the deployments that usually take the longest. 

```shell show_output=false
sleep 15
kubectl wait --for=condition=available deployment/argocd-dex-server -n argocd --timeout=300s
```

```shell show_output=false
kubectl wait --for=condition=available deployment/argocd-redis -n argocd --timeout=300s
```

```shell show_output=false
kubectl wait --for=condition=available deployment/argocd-server -n argocd --timeout=300s
```

> Patching ArgoCD server to NodePort

```shell show_output=false
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'
```

> Adding notification service

```shell show_output=false
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/notifications_catalog/install.yaml
```

> ArgoCD server is up and running
