# Install ArgoCD

Installs Argo CD in local k3d cluster

## Prerequisites
  
Make sure `kubectl` is connected to our k3d cluster.
  
```yaml instacli
Shell: kubectl config current-context
Expected output: k3d-xlrcluster
```

## Create namespace

First we have to create the `argocd` namespace in the k3d cluster. This is where ArgoCD will be installed.

We use `kubectl` to create the namespace.

```shell
kubectl create namespace argocd || true
```

## Install ArgoCD using kubectl

Use `kubectl` to install ArgoCD in the k3d cluster. The command will install ArgoCD in the `argocd` namespace and create a service account for it.

```yaml instacli
Print: Spinning up ArgoCD on cluster...
```
```shell
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
