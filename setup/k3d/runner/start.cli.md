# Install Runner

Installs Release runner in K3d

## Confirmation

```yaml instacli
Confirm: Set up runner in K3d?
```

## Install

Run the [install script](install.cli.md)

```yaml instacli
Run script: install.cli.md
```

## Graceful exit

Print a friendly message in case of an error or user cancelation

```yaml instacli
On error:
  Print: Release runner not installed
```
