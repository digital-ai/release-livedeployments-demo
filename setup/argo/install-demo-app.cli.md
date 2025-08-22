## Install demo application to ArgoCD

Installs the demo application to ArgoCD.

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

## Install demo application

Manually install the demo application to ArgoCD.

```yaml instacli
Print: Installing demo application to ArgoCD
```

```shell show_output=false
kubectl create namespace guestbook
```

```shell show_output=false
kubectl apply -n argocd -f setup/argo/guestbook-app.yaml
```

```yaml instacli
Print: Demo application will start in a few seconds
```