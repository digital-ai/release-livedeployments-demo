# Demo environment setup

Configures the demo environment with ArgoCD, Flux and more.  
Start by installing the k3d Kubernetes cluster.

## Components

- [k3d-cluster](k3d/cluster) - K3d - Lightweight Kubernetes in Docker - https://k3d.io
- [flux](flux) - Flux CD - GitOps for Kubernetes - https://fluxcd.io/
- [argo](argo) - ArgoCD - Declarative GitOps CD for Kubernetes - https://argo-cd.readthedocs.io/en/stable/
- [runner](k3d/runner) - Digital.ai Release Runner

## Setup

For an interactive experience, use [Instacli](https://github.com/Hes-Siemelink/instacli)

You can set up the components by invoking the command

    cli setup

This will show you the options to choose from:

```
Configures the demo environment with ArgoCD, Flux and more.

* Available commands: 
 > argo         Manages Argo CD installation and configuration
   flux         Manages Flux CD installation and configuration
   k3d          Manages K3d cluster and runner
   quickstart   Guides you through setting up all the components.
```

The `quickstart` option will walk you through the setup of all components in the right order.

## Helpful commands

Here are some commands that might be helpful to run:

Setting up the runner in k3d:

```shell
cli setup k3d cluster runner install
```

Removing the k3d cluster with everything in it:

```shell
cli setup k3d cluster delete
```

Interactive setup of Flux with configuration in Release:

```shell
cli setup k3d flux quickstart
```
