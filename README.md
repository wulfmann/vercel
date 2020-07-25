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

### DNS

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Record|X|https://vercel.com/docs/api#endpoints/dns/create-a-new-dns-record|
|Delete Record|X|https://vercel.com/docs/api#endpoints/dns/remove-a-dns-record|
|List Records||https://vercel.com/docs/api#endpoints/dns/list-all-the-dns-records-of-a-domain|
