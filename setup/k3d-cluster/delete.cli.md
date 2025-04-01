# Uninstall k3d cluster

Removes a k3d cluster from your local machine

## Precondition 

First we start by checking if the k3d command is available. If it is not, we print an error message and exit the script.

```yaml instacli
Shell: command -v k3d
On error:
  Print: |
    Please install k3d before running this script
    
    Install command:  brew install k3d
  Exit: 1
```

## Confirmation

Then we ask the user if they are sure they want to delete the k3d cluster. If the user answers "No", we print a message and exit the script.

```yaml instacli
Confirm: Are you sure you want to delete the k3d cluster?
```

## Actual deletion

Now we are ready to delete the k3d cluster. We do this by running the `k3d cluster delete` command.

```yaml instacli
Print: Deleting k3d cluster
Shell: k3d cluster delete xlrcluster
```
Finally, we print a message to confirm that the cluster has been deleted.

```yaml instacli
Print: Cluster deleted
```