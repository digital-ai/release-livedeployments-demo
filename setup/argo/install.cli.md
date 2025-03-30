# Install ArgoCD

Installs Argo CD in local k3d cluster

## Prerequisites
  
Make sure `kubectl` is connected to our k3d cluster.
  
```yaml instacli
Shell: kubectl config current-context
Expected output: k3d-xlrcluster
```

## Get credentials

Credentials are specified as input parameters to the script. If not specified, the script will prompt the user for them.
  
```yaml instacli
Script info:
  description: Configure Release to connect to ArgoCD
  input:
    password:
      description: New admin password for ArgoCD
      secret: true
```

## Install ArgoCD using kubectl

Use `kubectl` to install ArgoCD in the k3d cluster. The command will install ArgoCD in the `argocd` namespace and create a service account for it.

```yaml instacli
Shell: kubectl create namespace argocd
```

```yaml instacli
Print: Spinning up ArgoCD on cluster...
Shell:
  command: kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
  show output: true
```

To create the service account, we need to prepare the yaml patch the contains the password and the timestamp.

```yaml instacli
Set admin password: {}
```
