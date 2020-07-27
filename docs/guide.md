# Guide

You can view resource-specific documentation [here](/docs/reference/resources).

## Getting Started

```bash
pip install vercel
```

## Authentication

You can specify one or both of `api_token` and `team_id`:

```python
import vercel

vercel.api_token='xxx'
vercel.team_id='yyy' # optional
```

## Error Handling

All vercel error responses are surfaced as a `VercelError` object. This object contains `code` and `message` properties.

```python
import vercel
from vercel.exceptions import VercelError

try:
    vercel.User.get()
except VercelError as e:
    print(e.code)
    print(e.message)
```

## Low Level Access

You can use the lower level `make_request` and `make_paginated_request` methods to interact directly with the API wrapper.

```python
import vercel

vercel.api_token = 'xxx'

vercel.Request.make_request(
    method='GET',
    api_version='v2',
    resource='/domains/domain-id'
)
```
