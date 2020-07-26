from vercel.resources.base import Resource

class Deployment(Resource):
  def __init__(self, aliases, alias_assigned, alias_error, created_at, created_in, deployment_hostname, forced, id, meta, plan, private, ready_state, requested_at, target, team_id, type, url, user_id, regions, functions, routes, env, build, version):
    self.aliases = aliases
    self.alias_assigned = alias_assigned
    self.alias_error = alias_error
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
    self.version = version
    self.regions = regions
    self.functions = functions
    self.routes = routes
    self.env = env
    self.build = build
    self.version = version

  @classmethod
  def from_data(cls, data):
    aliases = data.get('alias', [])

    return cls(
      aliases=aliases,
      alias_assigned=data['aliasAssigned'],
      alias_error=data.get('aliasError'),
      created_at=data['createdAt'],
      created_in=data['createdIn'],
      deployment_hostname=data.get('deploymentHostname'),
      forced=data.get('forced'),
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
      user_id=data['userId'],
      regions=data.get('regions', []),
      functions=data.get('functions'),
      routes=data.get('routes'),
      env=data.get('env', []),
      build=data.get('build', { 'env': {} }),
      version=data.get('version')
    )
    
  @classmethod
  def get(cls, deployment_id=None, deployment_url=None, api_version='v11'):
      if deployment_id is None and deployment_url is None:
        raise Exception('one of deployment_id or deployment_url is required')
        
      if deployment_id is not None and deployment_url is not None:
        raise Exception('only one of deployment_id or deployment_url can be specified')
        
      resource = '/deployments'
      if deployment_id is not None:
        resource += f'/{deployment_id}'
          
      params = {} 
      if deployment_url is not None:
        params['url'] = deployment_url

      res = cls.make_request(
        method='GET',
        resource=resource,
        api_version=api_version,
        query_string=params
      )

      return cls.from_data(res)