# Connect GitHub repo

Connects local Flux to a GitHub repo.
The repository doesn't need to exist yet, it will be created if it doesn't.

## Prerequisites

### 1. Local k3d cluster

```yaml instacli
Run script: ../prerequisites/check-kubectl.cli.md
```

### 2. Flux command

```yaml instacli
Run script: ../prerequisites/check-flux.cli.md
```

## Get user information

```yaml instacli
Print: |
    You need a repository to work on. You can let Flux create a new one for you, or you can use an existing one.
    For the demo, it's best to fork the example repo https://github.com/digital-ai/release-fluxcd-demo
    
    You need to have a GitHub user and a personal access token. Make sure your token has `repo` scope (XXX Check this).
```

```yaml instacli
Script info:
  input:
    GITHUB_REPO: GitHub repo url (will create repo if not exists)
    GITHUB_USER: GitHub user
    GITHUB_TOKEN: User token to connect to GitHub
```

```yaml instacli
Prompt:
  description: Path in the repo to store the Flux configuration
  default: clusters/staging
```

## Flux bootstrap command

The `flux bootstrap` command is used to connect your local Flux installation to a GitHub repository.

```shell show_command=true
flux bootstrap github --owner=${GITHUB_USER} --repository=${GITHUB_REPO} --branch=main --personal --path=${output}
```

```yaml instacli
Print: |
  
  FluxCD configured successfully.
```