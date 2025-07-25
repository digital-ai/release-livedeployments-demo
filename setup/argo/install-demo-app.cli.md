## Install demo application to ArgoCD

Installs the demo application to ArgoCD.

## Prerequisites

```yaml instacli
Run script: ../prerequisites/check-kubectl.cli.md
```

## Install demo application

manually install the demo application to ArgoCD.

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
Print: Waiting for demo application to be ready
```

```shell show_output=false
sleep 15
kubectl wait --for=condition=available deployment/kustomize-guestbook-ui -n guestbook --timeout=300s
```

```yaml instacli
Print: Demo application is up and running
```