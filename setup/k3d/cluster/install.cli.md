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
    
    Install command:  brew install k3d
  Exit: 1
```

## Spin up cluster

```yaml instacli
Print: Spinning up k3d cluster
```

Use `k3d cluster create` to create a new cluster on your local machine.

```shell show_output=false
k3d cluster create democluster
```

Finally, we print a message to confirm that the cluster has been created.

```yaml instacli
Print: Cluster democluster created
```