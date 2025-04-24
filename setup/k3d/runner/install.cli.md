# Install Runner

Installs Release runner in K3d without user interaction.

## Create token

Call the `create-token.cli.md` script to create a token for the runner.

```yaml instacli
Run script: create-token.cli.md
As: ${token}
```

## Setup with xl kube

We can specify a minimal answer file for `xl kube` for a non-interactive setup:

```yaml instacli
Temp file:
  K8sSetup: PlainK8s
  ServerType: dai-release-runner
  RemoteRunnerReleaseUrl: 'http://release:5516'
  RemoteRunnerToken: ${token}
  RemoteRunnerReleaseName: k3d-runner
As: ${answers_file}
```

We invoke `xl kube install` with the options that pick default settings and prevent user interaction:

```shell
xl kube install --quick-setup --skip-prompts --answers ${answers_file}
```
