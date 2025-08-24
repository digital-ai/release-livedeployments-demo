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

```yaml instacli
Shell: |
  kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Clean up ArgoCD namespaces

```yaml instacli
Shell:
  command: kubectl delete namespace argocd
  show output: true
```

```yaml instacli
Shell:
  command: kubectl delete namespace guestbook
  show output: true
```