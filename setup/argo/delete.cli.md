# Delete ArgoCD

Deletes ArgoCD from the k3d cluster.

## Prerequisites

```yaml instacli
Check command:
  name: kubectl

Confirm: Are you sure you want to delete ArgoCD?
```

## Uninstall ArgoCD

> Removing ArgoCD from K3d cluster

Uninstall ArgoCD using the same manifest we installed it with

```shell show_output=false
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Clean up ArgoCD namespaces

```shell
kubectl delete namespace argocd
```

```shell
kubectl delete namespace guestbook
```