# Delete runner

Deletes Release runner from k3d cluster

```yaml instacli
Print: Deleting Release Runner from k3d cluster
```

## Use xl kube

The runner is deleted from the k3d cluster using the `xl kube` utility.

This is the minimal `answers.yaml` file that is needed:

```yaml file=answers.yaml
K8sSetup: PlainK8s
ServerType: dai-release-runner
RemoteRunnerReleaseName: k3d-runner
```

With this file you can run the `clean` command:

```shell show_output=false
./xlw kube clean --quick-setup --skip-prompts --answers "${SCRIPT_TEMP_DIR}/answers.yaml"
```

## Confirmation

```yaml instacli
Print: Runner deleted
```