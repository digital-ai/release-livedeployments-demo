# Demo environment setup

Configures the demo environment with ArgoCD, Flux and more.  
Start by installing the k3d Kubernetes cluster.

## Components

- [k3d-cluster](k3d-cluster) - K3d - Lightweight Kubernetes in Docker - https://k3d.io
- [flux](flux) - Flux CD - GitOps for Kubernetes - https://fluxcd.io/
- [argo](argo) - ArgoCD - Declarative GitOps CD for Kubernetes - https://argo-cd.readthedocs.io/en/stable/
- [runner](runner) - Digital.ai Release Runner

## Setup

For an interactive experience, use [Instacli](https://github.com/Hes-Siemelink/instacli)

You can set up the components individually by invoking the command

    cli setup

Or you can set up all components at once by invoking the command

    cli setup all

If you can't use Instacli, just follow the instructions in the individual setup files.