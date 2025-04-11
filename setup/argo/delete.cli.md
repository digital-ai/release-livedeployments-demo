# Delete ArgoCD

Deletes ArgoCD from the k3d cluster.

## Uninstall ArgoCD

Uninstall ArgoCD using the same manifest we installed it with

```shell
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Delete ArgoCD namespace

Then clean up the namespace

```shell
kubectl delete namespace argocd
```