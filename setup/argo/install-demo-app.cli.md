## Install demo application to ArgoCD

Installs the demo application to ArgoCD.

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

## Install demo application

> Installing demo application to ArgoCD

```yaml instacli
Shell: |
  kubectl create namespace guestbook
```

```yaml instacli
Shell: |
  kubectl apply -n argocd -f setup/argo/guestbook-app.yaml
```

> Demo application will start in a few seconds