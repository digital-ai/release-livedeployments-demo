# Install k3d cluster

Spins up a k3d cluster on your local machine

## Prerequisites

Check if the k3d command is available.

```shell show_output=false
command -v k3d
```

If not, print an error message and exit the script.

```yaml instacli
On error:
  Print: |
    Please install k3d before running this script

    Install command (macos):  brew install k3d
    Install command (linux):  curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
  Exit: 1
```

## Spin up cluster

```yaml instacli
Print: Spinning up k3d cluster 'democluster'
```

Use `k3d cluster create` to create a new cluster on your local machine.

```shell show_output=false
k3d cluster create democluster --network demo-network
```

```yaml instacli
Print: Waiting for k3d server
```

```shell show_output=false
kubectl wait --for=condition=Ready pod -l k8s-app=metrics-server -n kube-system --timeout=300s
```

Finally, we print a message to confirm that the cluster has been created.

```yaml instacli
Print: Cluster created
```