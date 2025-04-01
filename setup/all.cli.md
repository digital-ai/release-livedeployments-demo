# All-in-one setup

Set up of all the components in one go.

# K3d cluster setup

Create a K3d cluster

```yaml instacli
Confirm: Set up K3d?
      
Run script:
  resource: k3d-cluster/create.cli.md

On error:
  Print: K3d cluster not installed
```

# Runner setup

Install Digital.ai Release runner into the k3d cluster.

```yaml instacli
Confirm: Set up Release runner in K3d?
      
Run script:
  resource: runner/configure.cli

On error:
  Print: Release runner not installed in K3d
```

# ArgoCD setup

Install ArgoCD into cluster

```yaml instacli
Confirm: Set up ArgoCD?
      
Run script:
  resource: argo/install.cli.md
As: ${argocd}
```

Configure Digital.ai Release connection to ArgoCD

```yaml instacli
Run script:
  resource: argo/configure-release.md
  input:
    ${password}: ${argocd.password}

On error:
  Print: ArgoCD not installed
```

# Flux CD setup

Install Flux into cluster

```yaml instacli
Confirm: Set up FluxCD?
      
Run script:
  resource: flux/bootstrap.cli.md
```

Configure Digital.ai Release connection to Flux

```yaml instacli
Run script:
  resource: flux/configure-release.md

On error:
  Print: Flux CD not installed
```