# Install k3d cluster

Spins up a k3d cluster on your local machine

## Prerequisites

```yaml instacli
Check command:
  name: k3d
```

## Spin up cluster

Create a new cluster `democluster` in the `demo-network` Docker network.

> Spinning up k3d cluster 'democluster'

```yaml instacli
Shell: |
  k3d cluster create democluster --network demo-network
```

> Waiting for k3d server

```yaml instacli
Shell: |
  kubectl wait --for=condition=Ready pod -l k8s-app=metrics-server -n kube-system --timeout=300s
```

> Cluster created