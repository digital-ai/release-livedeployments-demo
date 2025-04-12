# Connect GitHub repo

Connects local Flux to a GitHub repo. 
The repository doesn't need to exist yet, it will be created if it doesn't.

## Prerequisites

First of all, you need to have your local k3d cluster running.  See [k3d cluster setup](../k3d/k3d-cluster) Make sure that it's your current cluster for `kubectl`.

```yaml instacli
Shell: kubectl config current-context
Expected output: k3d-xlrcluster
```

You need to have the `flux` command installed on our local machine.

```yaml instacli
Shell: command -v flux
On error:
  Print: |
    Please install Flux before running this script
    
    Install command:  brew install fluxcd/tap/flux
  Exit: 1
```

##  Get user information

You need a repository to work on. You can let Flux create a new one for you, or you can use an existing one. 
For the demo, it's best to fork the example repo https://github.com/jberta-agency04/release-fluxcd-demo

You need to have a GitHub user and a personal access token. Make sure your token has `repo` scope (XXX Check this).

```yaml instacli
Script info:
  input:
    GITHUB_REPO: GitHub repo url (will create repo if not exists)
    GITHUB_USER: GitHub user
    GITHUB_TOKEN: User token to connect to GitHub
```

## Flux bootstrap command
The `flux bootstrap` command is used to connect your local Flux installation to a GitHub repository. 

```shell
flux bootstrap github --owner=${GITHUB_USER} --repository=${GITHUB_REPO} --branch=main --personal --path=clusters/staging 
```