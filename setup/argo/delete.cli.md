# Delete ArgoCD

Deletes ArgoCD from the k3d cluster.

## Prerequisites

```yaml instacli
Run script: ../prerequisites/check-kubectl.cli.md
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