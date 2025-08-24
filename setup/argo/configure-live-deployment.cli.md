# Configure ArgoCD Live Deployment

Configure Release live deployments to connect to ArgoCD.

> Configuring Release Live Deployments for ArgoCD

```yaml instacli
Shell: |
  ./xlw apply -f setup/argo/argo-live-deployment.yaml
```

```yaml instacli
Shell: |
  ./xlw apply -f setup/argo/demo-live-deployment.yaml
```

> ArgoCD deployments added to release Live Deployments.