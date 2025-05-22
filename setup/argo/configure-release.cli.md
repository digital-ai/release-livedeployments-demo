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
      default: https://k3d-democluster-server-0
    ARGO_USERNAME: 
      description: Username
      default: admin
    ARGO_PASSWORD: 
      description: Password
      default: password
      secret: true
```

```yaml instacli
Shell: kubectl get svc argocd-server -n argocd -o jsonpath='{.spec.ports[0].nodePort}'
As: ${NODE_PORT}
```

## Configure Release

Use `xl` to configure the Release server using the yaml file [release-argo-config.yaml](release-argo-config.yaml). Connection details are passed using the `--values` option.

```shell show_output=false
./xlw apply -f setup/argo/release-argo-config.yaml --values argoCdServerUrl=${ARGO_URL}:${NODE_PORT} --values argoCdUsername=${ARGO_USERNAME} --values argoCdPassword=${ARGO_PASSWORD}
```

```yaml instacli
Print: | 
  ArgoCD API server added to release. 
  To get live deployment notifications save the YAML configuration from Live Deployments workflow into a file.
  After that run this command in terminal to apply it
  kubectl apply -n argocd -f notifications.yaml
```
