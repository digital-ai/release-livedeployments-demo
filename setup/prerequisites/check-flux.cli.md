## Prerequisite flux

Check if the flux command is available.

```shell show_output=false
command -v flux
```

If not, print an error message and exit the script.

```yaml instacli
On error:
  Error: |
    Please install Flux before running this script

    Install command (macos):  brew install fluxcd/tap/flux
    Install command (linux):  curl -s https://fluxcd.io/install.sh | sudo bash
```