# Install ArgoCD

Installs Argo CD in local k3d cluster

## Prerequisites

Check if the kubectl command is available.

```shell show_output=false
command -v kubectl
```

If not, print an error message and exit the script.

```yaml instacli
On error:
  Print: |
    Please install kubectl before running this script

    Install command (macos):  brew install kubectl
    Install command (linux):  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                              sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

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

```yaml instacli
Print: Waiting for ArgoCD server
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
