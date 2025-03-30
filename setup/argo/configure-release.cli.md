# Configure Release for ArgoCD

Configure Release to connect to ArgoCD.

## Get credentials

Credentials are specified as input parameters to the script. If not specified, the script will prompt the user for them.

```yaml instacli
Script info:
  description: Configure Release to connect to ArgoCD
  input:
    url: ArgoCD URL
    username: Username
    password: 
      description: Password
      secret: true
```

## Configure Release

Use `xl` to configure the Release server. Use the `--values` option to pass the certificate and key data to the command.

```yaml instacli
Shell:
  command: ./xlw apply -f setup/argo/release-argo-config.yaml --values fluxUrl=https://kubernetes.default.svc --values argoCdServerUrl=${input.url} --values argoCdUsername=${input.username} --values argoCdPassword=${input.password}
  show output: true
```
