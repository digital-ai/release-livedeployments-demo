# Install ArgoCD

Installs Argo CD in local k3d cluster

## Prerequisites
  
Make sure `kubectl` is connected to our k3d cluster.
  
```shell
kubectl config current-context
```
Should print:

```output
k3d-democluster
```

## Create namespace

First we have to create the `argocd` namespace in the k3d cluster. This is where ArgoCD will be installed.

We use `kubectl` to create the namespace.

```shell
kubectl create namespace argocd
```

## Install ArgoCD using kubectl

Use `kubectl` to install ArgoCD in the k3d cluster. The command will install ArgoCD in the `argocd` namespace and create a service account for it.

```yaml instacli
Print: Spinning up ArgoCD on K3d cluster
```

```shell show_output=false show_command=true
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
