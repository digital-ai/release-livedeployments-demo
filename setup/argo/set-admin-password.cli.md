# Sets ArgoCD admin password
  
Sets the admin password for ArgoCD. 

## Get the password

Credentials are specified as input parameters to the script. If not specified, the script will prompt the user for them.
 
```yaml instacli
Script info:
  description: Sets the admin password for ArgoCD
  input:
    password:
      description: New admin password for ArgoCD
      secret: true
```
  
## Configure ArgoCD with the admin password
   
To prepare the admin account, we need to create a yaml patch the contains the password and the timestamp.

The file [date.sh](date.sh) is a script that returns the current date in the format `YYYY-MM-DDTHH:MM:SS+TZ`.

We create a temporary patch file `argocd_secret_patch.json` that contains the password and the timestamp. 

```yaml instacli
Shell:
  resource: sh date.sh
As: ${date}

Output: |
  {
    "stringData": 
    {
      "admin.password": "${input.password}",
      "admin.passwordMtime": "${date}"
    }
  }
Save as: argocd_secret_patch.json
```
  
We can apply the patch to ArgoCD
  
```yaml instacli
Shell: 
  command: kubectl -n argocd patch secret argocd-secret --patch-file=argocd_secret_patch.json
  show output: true
```

Clean up the temporary patch file

```yaml instacli
Shell: rm argocd_secret_patch.json
```

## Exit with password

We exit with the password so that it can be used in the next step. This is not a good practice, but we do it for the sake of simplicity. In a real world scenario, you would use a secret management tool to store the password.
  
```yaml instacli
Output:
    password: ${input.password}
```
