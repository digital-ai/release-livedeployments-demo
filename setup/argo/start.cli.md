# ArgoCD setup

Set up of all the components in one go.


## User confirmation

```yaml instacli
Confirm: Set up ArgoCD?
```

## Install ArgoCD

Run install script

```yaml instacli
Run script: install.cli.md
As: ${argocd}
```

## Set admin password

To create the service account, we need to prepare the yaml patch the contains the password and the timestamp.

```yaml instacli
Set admin password: {}
As: ${password}
```

## Configure Release

Configure Digital.ai Release connection to ArgoCD

```yaml instacli
Configure release:
  password: ${password}
```

## Error handling

```yaml instacli
On error:
  Print: ArgoCD not installed
```
