# Configure Release for ArgoCD

Configure Release to connect to ArgoCD.

## Get credentials

Credentials are specified as input parameters to the script. If not specified, the script will prompt the user for them.

```yaml instacli
Script info:
  input:
    url: 
      description: ArgoCD URL
      default: https://argocd-server.argocd
    username: 
      description: Username
      default: admin
    password: 
      description: Password
      default: $2a$10$rRyBsGSHK6.uc8fntPwVIuLVHgsAhAX7TcdrqW/RADU0uh7CaChLa  # bcrypt hash of 'password'
      secret: true
```

## Configure Release

Use `xl` to configure the Release server. Use the `--values` option to pass the certificate and key data to the command.

```yaml instacli
Shell:
  command: ./xlw apply -f setup/argo/release-argo-config.yaml --values fluxUrl=https://kubernetes.default.svc --values argoCdServerUrl=${input.url} --values argoCdUsername=${input.username} --values argoCdPassword=${input.password}
  show output: true
```
