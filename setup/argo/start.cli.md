# ArgoCD setup

Set up of all the components in one go.

```yaml instacli
Confirm: Set up ArgoCD?
```

Run install script

```yaml instacli
Run script:
  resource: install.cli.md
As: ${argocd}
```

Configure Digital.ai Release connection to ArgoCD

```yaml instacli
Run script:
  resource: configure-release.cli.md
  input:
    ${password}: ${argocd.password}
```

Error handling

```yaml instacli
On error:
  Print: ArgoCD not installed
```
