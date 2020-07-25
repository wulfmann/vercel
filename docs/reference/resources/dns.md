# DNS

The [DNS API Operations]() have been grouped under the `Domain` object. The reason for this is you cannot perform a DNS operation without specifying the associated domain.

Requiring a `Domain` object first allows the API to remain simple and expected.

## Operations

### List Records

```python
domain = vercel.Domain.get('domainid')

records = domain.list_dns_records(
  limit=10,
  since='',
  until=''
)

for record in records.iter():
  print(record.id) # rec_xxx
```

[Learn More](/docs/reference/pagination) about how this library handles pagination.

### Create a Record

```python
domain = vercel.Domain.get('vercel.com')

record = domain.create_dns_record(
  name='api',
  type='CNAME',
  value='internal-api.vercel.com'
)

print(record.id) # rec_xxx
```

### Delete a Record

```python
domain = vercel.Domain.get('vercel.com')
record = domain.get_dns_record('rec_xxx')
record.delete()
```
