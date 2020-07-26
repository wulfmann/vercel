from vercel.resources.base import Resource

class Deployment(Resource):
  def __init__(self, aliases, alias_assigned, created_at, created_in, deployment_hostname, forced, id, meta, plan, private, ready_state, requested_at, target, team_id, type, url, user_id):
    self.aliases = aliases
    self.alias_assigned = alias_assigned
    self.created_at = created_at
    self.created_in = created_in
    self.deployment_hostname = deployment_hostname
    self.forced = forced
    self.id = id
    self.meta = meta
    self.plan = plan
    self.private = private
    self.ready_state = ready_state
    self.requested_at = requested_at
    self.target = target
    self.team_id = team_id
    self.type = type
    self.url = url
    self.user_id = user_id

  @classmethod
  def from_data(cls, data):
    aliases = data.get('alias', [])

    return cls(
      aliases=aliases,
      alias_assigned=data['aliasAssigned'],
      created_at=data['createdAt'],
      created_in=data['createdIn'],
      deployment_hostname=data['deploymentHostname'],
      forced=data['forced'],
      id=data['id'],
      meta=data['meta'],
      plan=data['plan'],
      private=data['private'],
      ready_state=data['readyState'],
      requested_at=data['requestedAt'],
      target=data['target'],
      team_id=data['teamId'],
      type=data['type'],
      url=data['url'],
      user_id=data['userId']
    )