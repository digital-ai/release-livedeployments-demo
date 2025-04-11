# Sets ArgoCD admin password
  
Sets the admin password for ArgoCD. 

## Get the password

Credentials are specified as input parameters to the script. If not specified, the script will prompt the user for them.
 
```yaml instacli
Script info:
  input:
    password:
      description: New admin password for ArgoCD
      default: password
      secret: true
```

## Hash the password

Use `htpasswd` to create the bcrypt hash of the password.

```yaml instacli
Shell:
  command: htpasswd -bnB  "" ${input.password}
  show output: false
As: ${password_hash}
```

## Configure ArgoCD with the admin password
   
To prepare the admin account, we need to create a yaml patch the contains the password hash and the timestamp.

We use the shell to return the current date in the format `YYYY-MM-DDTHH:MM:SS+TZ`.

We create a temporary file `${secret_patch}` that contains the password and the timestamp. 

```yaml instacli
Shell: echo $(date +%FT%T%Z)
As: ${date}

---
Temp file: |
  {
    "stringData": 
    {
      "admin.password": "${password_hash}",
      "admin.passwordMtime": "${date}"
    }
  }
As: ${secret_patch}
```

```shell
cat ${secret_patch}
```

We can apply the patch to ArgoCD
  
```shell
kubectl -n argocd patch secret argocd-secret --patch-file=${secret_patch}
```

## Exit with password

We exit with the password so that it can be used in the next step. This is not a good practice, but we do it for the sake of simplicity. In a real world scenario, you would use a secret management tool to store the password.
  
```yaml instacli
Output: ${input.password}
```
