# ArgoCD setup

Installs ArgoCD and configures Release.


## User confirmation

```yaml instacli
Confirm: |
  Set up ArgoCD?
  Note: Make sure to setup kubernetes first.
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

## Install demo application to ArgoCD

```yaml instacli
Run script: install-demo-app.cli.md
```

## Configure Release

Configure Digital.ai Release connection to ArgoCD

```yaml instacli
Configure release:
  password: ${password}
```

## Configure Release Live Deployments

Configure Digital.ai Release Live Deployments to use ArgoCD

```yaml instacli
Run script: configure-live-deployment.cli.md
```

## Error handling

```yaml instacli
On error:
  Print: ArgoCD not installed
```
