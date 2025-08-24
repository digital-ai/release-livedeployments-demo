# Uninstall k3d cluster

Removes the k3d cluster from your local machine

## Precondition

```yaml instacli
Check command:
  name: k3d

Confirm: Are you sure you want to delete the k3d cluster?
```

## Actual deletion

> Deleting k3d cluster

Use the following shell command to delete the cluster from your local machine:

```yaml instacli
Shell: |
  k3d cluster delete democluster
```

> Cluster deleted