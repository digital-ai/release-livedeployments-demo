# All-in-one setup

Set up of all the components in one go.

```yaml instacli
For each:
  ${script} in:
    - k3d-cluster/start.cli.md
    - runner/configure.cli
    - argo/start.cli.md
    - flux/start.cli.md
  Run script:
      resource: ${script}
```
