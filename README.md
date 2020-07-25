# Vercel Python SDK

## 🚨 This library is currently in alpha. Not many resources are supported and the core API is subject to change.

## Quickstart

### User Resources

```python
import vercel

vercel.api_key = 'xxxxxx'

vercel.Domain.create(
    domain_name='mydomain.com'
)
```

### Team Resources

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
