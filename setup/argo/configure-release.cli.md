# Configure Release for ArgoCD

Configure Release to connect to ArgoCD.

> Configuring Release for ArgoCD

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

> ArgoCD API server added to release.

## Configure Release for kubernetes

Also configure release to connect to kubernetes. This is needed to easily apply notifications for the ArgoCD

## Prerequisites

```yaml instacli
Check command:
  name: kubectl
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

## Configure Release

Use `xl` to configure the Release server. Use the `--values` option to pass the certificate and key data to the command.
The https://k3d-democluster-server-0 is used because it is an Docker container name that acts as a Kubernetes node
The port 6443 is the default port for the Kubernetes API server

```shell show_output=false
./xlw apply -f setup/argo/release-kube-config.yaml --values url=https://k3d-democluster-server-0:6443 --values clientCrt=${client_certificate_data} --values clientKey=${client_key_data}
```