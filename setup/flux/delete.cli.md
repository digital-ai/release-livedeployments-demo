# Uninstall flux cluster

Removes the flux cluster from your local machine and all the apps created by it

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

```yaml instacli
Check command:
  name: flux
```

```yaml instacli
Confirm: Are you sure you want to delete the flux cluster?
```

## Actual deletion

> Deleting flux cluster

Remove flux with the following command:

```shell show_output=false
flux uninstall --namespace=flux-system --silent
```

> Cluster deleted, please delete deployed apps manually