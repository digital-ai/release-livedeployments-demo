# Install Runner

Installs Release runner in K3d

## Confirmation

```yaml instacli
Confirm: Set up runner in K3d?
```

## Create token

Call the `create-token.cli.md` script to create a token for the runner.

```yaml instacli
Run script:
  resource: create-token.cli.md
As: ${token}
```

## xl kube setup

We can specifiy a minimal answer fil for `xl kube` that will provide a non-interactive setup:

```yaml instacli
Temp file:
  K8sSetup: PlainK8s
  ServerType: dai-release-runner
  RemoteRunnerReleaseUrl: 'http://host.k3d.internal:5516'
  RemoteRunnerToken: ${token}
As: ${answers_file}
```

We invoke `xl kube` install with the options that pick default settings and prevent user interaction:

```shell
xl kube install --quick-setup --skip-prompts --answers ${answers_file}
```

## Graceful exit

Print a friendly message in case of an error or user cancelation

```yaml instacli
On error:
  Print: Release runner not installed
```
