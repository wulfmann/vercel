# Vercel Python SDK

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

The following resources are supported by the sdk

