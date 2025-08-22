# Configure Release for Flux

Configure Release to connect to FluxCD.

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
```

## Get credentials

Use `kubectl` to get the connection certificate and key.

```yaml instacli
Shell: kubectl config view --raw -o jsonpath={.users[0].user.client-certificate-data}
As: ${client_certificate_data}
```

```yaml instacli
Shell: kubectl config view --raw -o jsonpath={.users[0].user.client-key-data}
As: ${client_key_data}
```

## Configure Release

Use `xl` to configure the Release server. Use the `--values` option to pass the certificate and key data to the command.
The https://k3d-democluster-server-0 is used because it is a Docker container name that acts as a Kubernetes node
The port 6443 is the default port for the Kubernetes API server

```shell show_output=false
./xlw apply -f setup/flux/release-flux-config.yaml --values fluxUrl=https://k3d-democluster-server-0:6443 --values fluxCertificate=${client_certificate_data} --values fluxKey=${client_key_data}
```
