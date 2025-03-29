# Install k3d cluster

Info for Instacli help:

```yaml instacli
Script info: Spins up a k3d cluster on your local machine
```

## Prerequisites

First we start by checking if the k3d command is available. If it is not, we give instructions on how to install it using brew and exit the script.

```yaml instacli
Shell: command -v k3d
On error:
  Print: |
    Please install `k3d` before running this script
    
    Install command:  brew install k3d
  Exit: 1
```

## Spin up cluster

Use `k3d cluster create` to create a new cluster on your local machine.

```yaml instacli
Print: Spinning up k3d cluster
Shell: k3d cluster create xlrcluster
```

Finally, we print a message to confirm that the cluster has been created.

```yaml instacli
Print: Cluster xlrcluster created
```