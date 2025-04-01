# Demo environment setup

Configures the demo environment with ArgoCD, Flux and more.  
Start by installing the k3d Kubernetes cluster.

## Components

- [k3d](k3d) - K3d - Lightweight Kubernetes in Docker - https://k3d.io
- [flux](flux) - Flux CD - GitOps for Kubernetes - https://fluxcd.io/
- [argo](argo) - ArgoCD - Declarative GitOps CD for Kubernetes - https://argo-cd.readthedocs.io/en/stable/
- [runner](runner) - Digital.ai Release Runner

## Setup

Start by installing the k3d Kubernetes cluster, it is needed by both the Flux and ArgoCD components.

* [Install k3d](k3d/install.cli.md)

