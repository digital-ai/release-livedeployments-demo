# Install Runner

Installs Release runner in K3d without user interaction.

## Create token

Call the `create-token.cli.md` script to create a token for the runner.

```yaml instacli
Run script: create-token.cli.md
As: ${token}
```

## Setup with xl kube

```yaml instacli
Print: Installing Release Runner into k3d cluster
```

We can specify a minimal `answers.yaml` file for `xl kube` for a non-interactive setup:

```yaml file=answers.yaml resolve=true
K8sSetup: PlainK8s
ServerType: dai-release-runner
RemoteRunnerReleaseUrl: 'http://host.k3d.internal:5516'
RemoteRunnerToken: ${token}
RemoteRunnerReleaseName: k3d-runner
```

Invoke `xl kube install` with this file. In combination with `--quick-setup` to use default settings and `--skip-prompts` to prevent user interaction, the installation is quick and easy.

```shell cd=${SCRIPT_TEMP_DIR} show_output=false
xl kube install --quick-setup --skip-prompts --answers answers.yaml
```
Print confirmation message when done.

```yaml instacli
Print: Release runner installed
```