# Delete runner

Deletes Release runner from k3d cluster

The runner is deleted from the k3d cluster using the `xl kube` utility.

This is the minimal answers file that is needed:

```yaml instacli
Temp file:
  K8sSetup: PlainK8s
  ServerType: dai-release-runner
As: ${answers_file}
```

With this file you can run the `clean` command:

```shell
xl kube clean --quick-setup --skip-prompts --answers ${answers_file}
```
