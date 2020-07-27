# Authentication

There are [two relevant](https://vercel.com/docs/api#api-basics/authentication) values for a Vercel API request:

|Key|Required|
|------|------|
|api_key|X|
|team_id|

An `api_key` can be generated from your [user settings](https://vercel.com/account) page. This key has permission to do anything your user can do, but on it's own it cannot perform any operation on your team's resources.

To perform an operation on a resource that is owned by a team, you must specify the `team_id`. This can be your team slug or the internal id of your team. You can learn how to find your team id [here](https://vercel.com/docs/api#api-basics/authentication/accessing-resources-owned-by-a-team).

## Usage

You can set an `api_key` or `team_id` on any operation by passing them in as keyword arguments:

```python
import vercel

vercel.Deployment.get(
  '',
  api_key='xxx',
  team_id='yyy'
)
```

You can also set these globally:

```python
import vercel

vercel.api_key='xxx'
vercel.team_id='yyy'

vercel.Deployment.get('')
```
