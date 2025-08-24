# Sets ArgoCD admin password

Sets the admin password for ArgoCD.

## Configure ArgoCD with the admin password

To prepare the admin account, we need to create a yaml patch the contains the password hash and the timestamp.

We use the shell to return the current date in the format `YYYY-MM-DDTHH:MM:SS+TZ`.

We create a temporary file `${secret_patch}` that contains the password and the timestamp.

For now we use the default password `password` and send the hash in the patch.

```yaml instacli
Shell: echo $(date +%FT%T%Z)
As: ${date}

---
Temp file: |
  {
    "stringData": 
    {
      "admin.password": "$2a$10$rRyBsGSHK6.uc8fntPwVIuLVHgsAhAX7TcdrqW/RADU0uh7CaChLa",
      "admin.passwordMtime": "${date}"
    }
  }
As: ${secret_patch}
```

We can apply the patch to ArgoCD

```yaml instacli
Shell:
  command: kubectl -n argocd patch secret argocd-secret --patch-file=${secret_patch}
  show output: true
```
