# Configure Release for Flux

Adds configuration to Release to connect to FluxCD servers.

## Get data from Flux system

We use `kubectl` to get the connection certificate and key.

```yaml instacli
Shell: kubectl config view --raw -o jsonpath='{.users[0].user.client-certificate-data}'
As: ${client-certificate-data}
```

```yaml instacli
Shell: kubectl config view --raw -o jsonpath='{.users[0].user.client-key-data}'
As: ${client-key-data}
```

## Configure Release

Use `xl` to configure the Release server.

<!-- yaml instacli before
# Hack to fix quotes
Replace:  
  text: "'"
  in: ${client-certificate-data}
  replace with: ""
As: ${client-certificate-data}
---
Replace:
  text: "'"
  in: ${client-key-data}
  replace with: ""
As: ${client-key-data}
-->

```yaml instacli
Shell: ./xlw apply -f setup/flux/release-flux-config.yaml --values fluxUrl=https://kubernetes.default.svc --values fluxCertificate=${client-certificate-data} --values fluxKey=${client-key-data}
Print: ${output}
```
