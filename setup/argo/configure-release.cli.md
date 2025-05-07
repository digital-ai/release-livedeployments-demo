# Configure Release for ArgoCD

Configure Release to connect to ArgoCD.

```yaml instacli
Print: Configuring Release for ArgoCD
```

## Get credentials

We use default credentials to connect to ArgoCD. 

```yaml instacli
Script info:
  input:
    ARGO_URL: 
      description: ArgoCD URL
      default: https://argocd-server.argocd
    ARGO_USERNAME: 
      description: Username
      default: admin
    ARGO_PASSWORD: 
      description: Password
      default: password
      secret: true
```

## Configure Release

Use `xl` to configure the Release server using the yaml file [release-argo-config.yaml](release-argo-config.yaml). Connection details are passed using the `--values` option.

```shell show_output=false
./xlw apply -f setup/argo/release-argo-config.yaml --values argoCdServerUrl=${ARGO_URL} --values argoCdUsername=${ARGO_USERNAME} --values argoCdPassword=${ARGO_PASSWORD}
```

