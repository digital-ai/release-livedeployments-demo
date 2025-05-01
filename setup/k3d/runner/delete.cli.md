# Delete runner

Deletes Release runner from k3d cluster

The runner is deleted from the k3d cluster using the `xl kube` utility.

This is the minimal `answers.yaml` file that is needed:

```yaml file=answers.yaml
K8sSetup: PlainK8s
ServerType: dai-release-runner
RemoteRunnerReleaseName: k3d-runner
```

With this file you can run the `clean` command:

```shell cd=${SCRIPT_TEMP_DIR}
xl kube clean --quick-setup --skip-prompts --answers answers.yaml
```
