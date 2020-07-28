# Vercel Python SDK

## 🚨 This library is currently in beta 🚨

Most resources are supported, but some are missing. You can check the [support table](/docs/supported-resources.md) for an up-to-date list.

## Install

Requires >= python 3.7

```bash
pip install vercel
```

## Quickstart

```python
import vercel

vercel.api_token = 'xxxxxx'

user = vercel.User.get()
```

### Team Resources

To access resources owned by a team, set the `team_id`.

You can learn more about the authentication process [here](/docs/reference/authentication).

```python
import vercel

vercel.api_token = 'xxxxxx'
vercel.team_id = 'my-team

vercel.Domain.get('mydomain.com')
```

## Guide

You can view more information on working with this library in [the guide](/docs/guide).

## Resource Support

See the [support table](/docs/supported-resources) for an up-to-date list of the API resources this library supports.

If you'd like to see a resource support prioritized, [open an issue](https://github.com/wulfmann/vercel/issues/new/choose).

## Contributing

Want to contribute or found a bug to fix?

Checkout the [contributing doc](/CONTRIBUTING.md) and submit a PR!
