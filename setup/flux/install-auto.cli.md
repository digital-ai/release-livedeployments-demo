# Install FluxCD with demo apps

Install FluxCD and creates demo applications automatically.

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

```yaml instacli
Check command:
  name: flux
```

## Install flux

> Installing FluxCD

```shell show_output=false
flux install
```

## Create podinfo namespace

> Creating podinfo app

```shell show_output=false
kubectl create namespace podinfo
```

## Create podinfo git source

```shell show_output=false
flux create source git podinfo \
  --url=https://github.com/stefanprodan/podinfo \
  --branch=master \
  --interval=5m \
  --namespace=podinfo
```

## Create podinfo kustomization

```shell show_output=false
flux create kustomization podinfo \
  --source=GitRepository/podinfo \
  --path="./kustomize" \
  --namespace=podinfo \
  --target-namespace=podinfo \
  --prune=true \
  --interval=5m
```

> FluxCD configured successfully.