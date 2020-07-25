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

### User

|Operation|Supported|Reference|
|---------|---------|-------------|
|Get User|❌|[Vercel](https://vercel.com/docs/api#endpoints/user)|

### Deployments

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Deployment|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/create-a-new-deployment)|
|Upload Deployment Files|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/upload-deployment-files)|
|List Deployments|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/list-deployments)|
|Get Deployment|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/get-a-single-deployment)|
|Delete Deployment|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/delete-a-deployment)|
|List DeploymentFiles|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/list-deployment-files)|
|Get Single File Contents|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/get-single-file-contents)|
|List Builds|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/list-builds)|
|Cancel Deployment|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/cancel-a-deployment)|

### Logs

|Operation|Supported|Reference|
|---------|---------|-------------|
|Get Build Logs|❌|[Vercel](https://vercel.com/docs/api#endpoints/logs/get-build-logs)|
|Stream Serverless Function Logs|❌|[Vercel](https://vercel.com/docs/api#endpoints/logs/stream-serverless-function-logs)|
|Fetch Failed Requests For Serverless Function|❌|[Vercel](https://vercel.com/docs/api#endpoints/logs/fetch-failed-requests-for-serverless-function)|

### Domains

|Operation|Supported|Reference|
|---------|---------|-------------|

### DNS

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Record|✅|[Vercel](https://vercel.com/docs/api#endpoints/dns/create-a-new-dns-record)|
|Delete Record|✅|[Vercel](https://vercel.com/docs/api#endpoints/dns/remove-a-dns-record)|
|List Records|❌|[Vercel](https://vercel.com/docs/api#endpoints/dns/list-all-the-dns-records-of-a-domain)|

### Certificates

|Operation|Supported|Reference|
|---------|---------|-------------|

### Aliases

|Operation|Supported|Reference|
|---------|---------|-------------|

### Secrets

|Operation|Supported|Reference|
|---------|---------|-------------|

### Teams

|Operation|Supported|Reference|
|---------|---------|-------------|

### Projects

|Operation|Supported|Reference|
|---------|---------|-------------|

### Authentication

|Operation|Supported|Reference|
|---------|---------|-------------|

### Oauth2

|Operation|Supported|Reference|
|---------|---------|-------------|

### Webhooks

|Operation|Supported|Reference|
|---------|---------|-------------|

### Log Drains

|Operation|Supported|Reference|
|---------|---------|-------------|