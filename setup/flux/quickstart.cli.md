# Flux CD setup

Setup of all needed components in one go

```yaml instacli
Confirm: Set up FluxCD?
```

```yaml instacli
Prompt:
  description: |
    Do you want to use manual setup or automated?
        * Automated will create a Flux environment with demo app without using a GitHub repository
        * Manual will need GitHub repo and GitHub user data provided for bootstrapping
  enum:
    - Automated
    - Manual
```

```yaml instacli
If:
  item: ${output}
  equals: Manual
  then:
    Run script: bootstrap.cli.md
  else:
    Run script: install-auto.cli.md
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