# Demo environment setup

Configures the demo environment witih ArgoCD, Flux and more.

## Components

- [k3d](k3d) - Lightweight Kubernetes in Docker - https://k3d.io
- [Flux](flux) - GitOps for Kubernetes - https://fluxcd.io/
- [ArgoCD](argo) - Declarative GitOps CD for Kubernetes - https://argo-cd.readthedocs.io/en/stable/
- [runner](runner) - Digital.ai Release Runner

## Setup

Start by installing the k3d Kubernetes cluster, it is needed by both the Flux and ArgoCD components.

* [Install k3d](k3d/install.cli.md)

