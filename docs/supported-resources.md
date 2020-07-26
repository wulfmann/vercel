# Supported Resources

The following is a table of all of the API resources from Vercel, along with this libraries level of support.

## Operations

### User

|Operation|Supported|Reference|
|---------|---------|-------------|
|Get User|✅|[Vercel](https://vercel.com/docs/api#endpoints/user)|

### Deployments

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Deployment|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/create-a-new-deployment)|
|Upload Deployment Files|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/upload-deployment-files)|
|List Deployments|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/list-deployments)|
|Get Deployment|✅|[Vercel](https://vercel.com/docs/api#endpoints/deployments/get-a-single-deployment)|
|Delete Deployment|✅|[Vercel](https://vercel.com/docs/api#endpoints/deployments/delete-a-deployment)|
|List DeploymentFiles|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/list-deployment-files)|
|Get Single File Contents|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/get-single-file-contents)|
|List Builds|❌|[Vercel](https://vercel.com/docs/api#endpoints/deployments/list-builds)|
|Cancel Deployment|✅|[Vercel](https://vercel.com/docs/api#endpoints/deployments/cancel-a-deployment)|

### Logs

|Operation|Supported|Reference|
|---------|---------|-------------|
|Get Build Logs|❌|[Vercel](https://vercel.com/docs/api#endpoints/logs/get-build-logs)|
|Stream Serverless Function Logs|❌|[Vercel](https://vercel.com/docs/api#endpoints/logs/stream-serverless-function-logs)|
|Fetch Failed Requests For Serverless Function|❌|[Vercel](https://vercel.com/docs/api#endpoints/logs/fetch-failed-requests-for-serverless-function)|

### Domains

|Operation|Supported|Reference|
|---------|---------|-------------|
|List Domains|❌||
|Create Domain|✅||
|Transfer in a  Domain|❌||
|Verify Domain|❌||
|Get Domain|❌||
|Delete Domain|❌||
|Check Domain Availability|❌||
|Check Domain Price|❌||
|Purchase Domain|❌||

### DNS

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Record|✅|[Vercel](https://vercel.com/docs/api#endpoints/dns/create-a-new-dns-record)|
|Delete Record|✅|[Vercel](https://vercel.com/docs/api#endpoints/dns/remove-a-dns-record)|
|List Records|❌|[Vercel](https://vercel.com/docs/api#endpoints/dns/list-all-the-dns-records-of-a-domain)|

### Certificates

|Operation|Supported|Reference|
|---------|---------|-------------|
|List Certificates|❌||
|Get Certificate|❌||
|Create Certificate|❌||
|Submit Certificate|❌||
|Delete Certificate|❌||

### Aliases

|Operation|Supported|Reference|
|---------|---------|-------------|
|List Aliases|❌||
|Get Alias|❌||
|Delete Alias|❌||
|Purge Alias|❌||
|List Aliases By Deployment|❌||
|Assign Alias To Deployment|❌||

### Secrets

|Operation|Supported|Reference|
|---------|---------|-------------|
|List Secrets|❌||
|Get Secret|❌||
|Create Secret|❌||
|Change Secret Name|❌||
|Delete Secret|❌||

### Teams

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Team|❌||
|Delete Team|❌||
|List Teams|❌||
|Get Team|❌||
|Update Team|❌||
|List Team Members|❌||
|Invite User To Team|❌||
|Change User Role Or Status|❌||
|Request To Join Team|❌||
|Check Status Of Join Request|❌||
|Remove User From Team|❌||

### Projects

|Operation|Supported|Reference|
|---------|---------|-------------|
|Create Project|✅||
|Ensure Project Exists|❌||
|Get Project|✅||
|List Projects|❌||
|Update Project|❌||
|Delete Project|❌||
|List Project Environment Variables|❌||
|Create Project Environment Variable|❌||
|Delete Project Environment Variable|❌||
|Add Domain To Project|❌||
|Set Redirect For Domain|❌||
|Delete Production Domain For Project|❌||

### Authentication

|Operation|Supported|Reference|
|---------|---------|-------------|
|Request Login|❌||
|Verify Login|❌||

### Oauth2

|Operation|Supported|Reference|
|---------|---------|-------------|

### Webhooks

|Operation|Supported|Reference|
|---------|---------|-------------|
|List Webhooks|❌||
|Create Webhook|❌||
|Delete Webhook|❌||

### Log Drains

|Operation|Supported|Reference|
|---------|---------|-------------|
|List Log Drains|❌||
|Create Log Drain|❌||
|Delete Log Drain|❌||