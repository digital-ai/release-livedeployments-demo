# Configure Release for Flux

Configure Release to connect to FluxCD.

## Prerequisites

Make sure `kubectl` is connected to our k3d cluster.

```shell
kubectl config current-context
```

should give you the following output:

```output
k3d-democluster
```

## Get credentials

We use `kubectl` to get the connection certificate and key.

```yaml instacli
Shell: kubectl config view --raw -o jsonpath={.users[0].user.client-certificate-data}
As: ${client_certificate_data}
```

```yaml instacli
Shell: kubectl config view --raw -o jsonpath={.users[0].user.client-key-data}
As: ${client_key_data}
```

```yaml instacli
Shell: kubectl config view --raw -o jsonpath={.clusters[0].cluster.server}
As: ${flux_url}
```

```yaml instacli
Shell: echo "${flux_url}" | sed 's/0.0.0.0/host.k3d.internal/'
As: ${flux_url}
```

## Configure Release

Use `xl` to configure the Release server. Use the `--values` option to pass the certificate and key data to the command.

```shell show_output=false
./xlw apply -f setup/flux/release-flux-config.yaml --values fluxUrl=${flux_url} --values fluxCertificate=${client_certificate_data} --values fluxKey=${client_key_data}
```
