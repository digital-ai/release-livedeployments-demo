# Install FluxCD with demo apps

Install FluxCD and creates demo applications automatically.

## Prerequisites

### 1. Local k3d cluster

```yaml instacli
Run script: ../prerequisites/check-kubectl.cli.md
```

### 2. Flux command

```yaml instacli
Run script: ../prerequisites/check-flux.cli.md
```

## Install flux

```yaml instacli
Print: Installing FluxCD
```

```shell show_output=false
flux install
```

```yaml instacli
Print: Creating podinfo app
```

## Create podinfo namespace

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

```yaml instacli
Print: Waiting for demo application to be ready
```

```shell show_output=false
sleep 15
kubectl wait --for=condition=available deployment/podinfo -n podinfo --timeout=300s
```

```yaml instacli
Print: |
  
  FluxCD configured successfully.
```