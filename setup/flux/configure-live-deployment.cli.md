# Configure FluxCD Live Deployment

Configure Release live deployments to connect to FluxCD.

```yaml instacli
Print: Configuring Release Live Deployments for FluxCD
```

```shell show_output=false
./xlw apply -f setup/flux/flux-live-deployment.yaml
```

```shell show_output=false
./xlw apply -f setup/flux/demo-live-deployment.yaml
```

```yaml instacli
Print: |
  
  FluxCD deployments added to release Live Deployments.
```