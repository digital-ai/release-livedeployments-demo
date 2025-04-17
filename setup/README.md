# Demo environment setup

Configures the demo environment with ArgoCD, Flux and more.  
Start by installing the k3d Kubernetes cluster.

## Components

- [k3d-cluster](k3d/cluster) - K3d - Lightweight Kubernetes in Docker - https://k3d.io
- [flux](flux) - Flux CD - GitOps for Kubernetes - https://fluxcd.io/
- [argo](argo) - ArgoCD - Declarative GitOps CD for Kubernetes - https://argo-cd.readthedocs.io/en/stable/
- [runner](k3d/runner) - Digital.ai Release Runner

## Prerequisites

* Java 17 or higher
* The `k3d` utility
* The `flux` utility

## Setup

For an interactive experience, use [Instacli](https://github.com/Hes-Siemelink/instacli). Launch Instacli by invoking the `./cli` command. This will download Instacli if not already present.

If you can't run Instacli, just browse the markdown files in this directory and subdirectories. They contain detailed instructions and the same commands as the Instacli scripts. In fact, the markdown files *are* the Instacli scripts! 😲🤔

Let's start from the top:

```shell
./cli setup
```

You will be shown the options to choose from:

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
./cli setup k3d cluster runner install
```

Removing the k3d cluster with everything in it:

```shell
./cli setup k3d cluster delete
```

Interactive setup of Flux with configuration in Release:

```shell
./cli setup k3d flux quickstart
```
