# Uninstall flux cluster

Removes the flux cluster from your local machine and all the apps created by it

## Prerequisites

### 1. Local k3d cluster

Make sure `kubectl` is connected to our k3d cluster.

```shell
kubectl config current-context
```

Should print:

```output
k3d-democluster
```

### 2. Flux command

You need to have the `flux` command installed on our local machine.

```shell show_output=false
command -v flux
```

If not, print an error message and exit the script.

```yaml instacli
On error:
  Print: |
    Please install Flux before running this script

    Install command (macos):  brew install fluxcd/tap/flux
    Install command (linux):  curl -s https://fluxcd.io/install.sh | sudo bash
  Exit: 1
```

## Confirmation

Then we ask the user if they are sure they want to delete the flux cluster. If the user answers "No", we print a message and exit the script.

```yaml instacli
Confirm: Are you sure you want to delete the flux cluster?
```

## Actual deletion

Now we are ready to delete the flux cluster.

```yaml instacli
Print: Deleting flux cluster
```

We do this by running the `flux uninstall` command.

```shell show_output=false
flux uninstall --namespace=flux-system --silent

```

Finally, we print a message to confirm that the cluster has been deleted.

```yaml instacli
Print: Cluster deleted, please delete deployed apps manually
```