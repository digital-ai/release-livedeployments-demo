# Configure ArgoCD Live Deployment

Configure Release live deployments to connect to ArgoCD.

```yaml instacli
Print: Configuring Release Live Deployments for ArgoCD
```

```shell show_output=false
./xlw apply -f setup/argo/argo-live-deployment.yaml
```

```shell show_output=false
./xlw apply -f setup/argo/demo-live-deployment.yaml
```

```yaml instacli
Print: |
  
  ArgoCD deployments added to release Live Deployments.
```