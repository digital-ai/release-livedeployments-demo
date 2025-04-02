# Create Runner Token

Creates a token in Release for the Runner.

```yaml instacli
Shell: date
As: ${date}

Print: Creating token for Runner in Digital.ai Release
POST:
  url: http://localhost:5516/api/v1/personal-access-tokens
  username: admin
  password: admin
  body:
    tokenNote: ${date}
    globalPermissions: 
    - runner#registration

Output: ${output.token}
```