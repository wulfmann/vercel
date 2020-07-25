# Vercel Python SDK

## 🚨 This library is currently in alpha. Not many resources are supported and the core API is subject to change.

## Install

Requires >= python 3.7

```bash
pip install vercel
```

## Quickstart

```python
import vercel

vercel.api_key = 'xxxxxx'

user = vercel.User.get()

print(user.name) # example
```

### Team Resources

To access resources owned by a team, set the `team_id`.

You can learn more about the authentication process [here](/docs/reference/authentication).

```python
import vercel

vercel.api_key = 'xxxxxx'
vercel.team_id = 'my-team

vercel.Domain.create(
    domain_name='mydomain.com'
)
```

## Resource Support

See the [support table](/docs/supported-resources.md) for an up-to-date list of the API resources this library supports.

## Contributing

Want to contribute or found a bug to fix?

Checkout the [contributing doc](/CONTRIBUTING.md) and submit a PR!
