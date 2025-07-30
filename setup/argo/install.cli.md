# Install ArgoCD

Installs Argo CD in local k3d cluster

## Prerequisites

```yaml instacli
Run script: ../prerequisites/check-kubectl.cli.md
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

```shell show_output=false
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

```yaml instacli
Print: Waiting for ArgoCD server
```

Wait for two usually the longest taking deployments

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

```yaml instacli
Print: Patching ArgoCD server to NodePort
```

```shell show_output=false
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'
```

```yaml instacli
Print: Adding notification service
```

```shell show_output=false
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/notifications_catalog/install.yaml
```

```yaml instacli
Print: ArgoCD server is up and running
```
