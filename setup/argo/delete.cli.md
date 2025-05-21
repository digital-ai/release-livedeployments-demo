# Delete ArgoCD

Deletes ArgoCD from the k3d cluster.

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

## Uninstall ArgoCD

Uninstall ArgoCD using the same manifest we installed it with

```yaml instacli
Print: Removing ArgoCD from K3d cluster
```

```shell show_output=false
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Delete ArgoCD namespace

Then clean up the namespace

```shell
kubectl delete namespace argocd
```