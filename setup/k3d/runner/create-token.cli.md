# Create Runner Token

Creates a token in Release for the Runner.

```yaml instacli
Print: Creating token for Runner in Digital.ai Release
```

First, get a unique identifier for the token.

```yaml instacli
Shell: date
As: ${date}
```

Now we can make the call

```yaml instacli
POST:
  url: http://release:5516/api/v1/personal-access-tokens
  username: admin
  password: admin
  body:
    tokenNote: K3d runner ${date}
    globalPermissions: 
    - runner#registration

Output: ${output.token}
```