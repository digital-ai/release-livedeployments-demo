# Flux CD setup

Set up of all the components in one go.

```yaml instacli
Confirm: Set up FluxCD?
```

Install Flux

```yaml instacli
Run script:
  resource: bootstrap.cli.md
```

Configure Digital.ai Release connection to Flux

```yaml instacli
Run script:
  resource: configure-release.cli.md
```

Error handling

```yaml instacli
On error:
  Print: Flux CD not installed
```