## Install demo application to ArgoCD

Installs the demo application to ArgoCD.

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

## Install demo application

> Installing demo application to ArgoCD

```shell show_output=false
kubectl create namespace guestbook
```

```shell show_output=false
kubectl apply -n argocd -f setup/argo/guestbook-app.yaml
```

> Demo application will start in a few seconds