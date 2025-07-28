# Flux CD setup

Set up of all the components in one go.

```yaml instacli
Confirm: Set up FluxCD?
```

Install Flux

```yaml instacli
Run script: bootstrap.cli.md
```

Configure Digital.ai Release connection to Flux

```yaml instacli
Run script: configure-release.cli.md
```

## Configure Release Live Deployments

Configure Digital.ai Release Live Deployments to use FluxCD

```yaml instacli
Run script: configure-live-deployment.cli.md
```

Error handling

```yaml instacli
On error:
  Print: Flux CD not installed
```