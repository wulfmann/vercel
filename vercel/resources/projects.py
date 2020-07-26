from vercel.resources.base import Resource
from vercel.resources.deployments import Deployment

class Alias:
  def __init__(self, domain, target, created_at, configured_by, configured_changed_at):
    self.domain = domain
    self.target = target
    self.created_at = created_at
    self.configured_by = configured_by
    self.configured_changed_at = configured_changed_at

  @classmethod
  def from_data(cls, data):
    return cls(
      domain=data['domain'],
      target=data['target'],
      created_at=data['createdAt'],
      configured_by=data['configuredBy'],
      configured_changed_at=data['configuredChangedAt']
    )

class EnvironmentVariable(Resource):
  def __init__(self, project_id, key, value, configuration_id, updated_at, created_at):
    self.project_id = project_id
    self.key = key
    self.value = value
    self.configuration_id = configuration_id
    self.updated_at = updated_at
    self.created_at = created_at

  @classmethod
  def from_data(cls, project_id, data):
    return cls(
      project_id=project_id,
      key=data['key'],
      value=data['value'],
      configuration_id=data['configurationId'],
      updated_at=data['updatedAt'],
      created_at=data['createdAt']
    )

  def delete(self, api_version='v'):
    res = self.make_request(
      method='DELETE',
      resource=f'',
      api_version=api_version
    )

class Project(Resource):
    def __init__(self, id, name, aliases, account_id, updated_at, created_at, latest_deployments, production_deployment, environment_variables):
        self.id = id
        self.name = name
        self.aliases = aliases
        self.account_id = account_id
        self.updated_at = updated_at
        self.created_at = created_at
        self.latest_deployments = latest_deployments
        self.production_deployment = production_deployment
        self.environment_variables = environment_variables
        
    def update_from_data(self, data):
      return self
        
    @classmethod
    def from_data(cls, data):
      project_id = data['id']

      # Aliases
      aliases = [
        Alias.from_data(alias)
        for alias in data.get('alias', [])
      ]

      # Production Deployment
      target = data.get('targets', {})
      production = target.get('production')
      
      if production is not None:
        production = Deployment.from_data(production)
      
      # Environment Variables
      environment_variables = [
        EnvironmentVariable.from_data(project_id, env)
        for env in data.get('env', [])
      ]
      
      # Latest Deployments
      latest_deployments = [
        Deployment.from_data(deployment)
        for deployment in data.get('latestDeployments', [])
      ]
      
      return cls(
        id=project_id,
        name=data['name'],
        aliases=aliases,
        account_id=data['accountId'],
        updated_at=data['updatedAt'],
        created_at=data['createdAt'],
        latest_deployments=latest_deployments,
        production_deployment=production,
        environment_variables=environment_variables
      )

    @classmethod
    def get(cls, identifier, api_version='v1'):
        res = cls.make_request(
          method='GET',
          resource=f'/projects/{identifier}',
          api_version=api_version
        )
        return cls.from_data(res)
        
    @classmethod
    def create(cls, name, api_version='v1'):
        res = cls.make_request(
          method='POST',
          resource=f'/projects',
          api_version=api_version,
          data={
            'name': name
          }
        )
        return cls.from_data(res)
        
    @classmethod
    def list(cls, api_version='v4'):
        res = cls.make_request(
          method='GET',
          resource=f'/projects',
          api_version=api_version
        )
        # todo pagination
        return cls.from_data(res)
        
    def update(self, framework=None, public_source=None, build_command=None, dev_command=None, output_directory=None, root_directory=None, api_version='v2'):
        res = cls.make_request(
          method='PATCH',
          resource=f'/projects/{self.id}',
          data={}
        )
        
        self.update_from_data(res)
        
        return self
        
    def delete(self, api_version='v2'):
        cls.make_request(
          method='DELETE',
          resource=f'/projects/{self.id}',
          api_version=api_version
        )
        
    def get_environment_variables(self, api_version='v5'):
        res = cls.make_request(
          method='GET',
          resource=f'/projects/{self.id}/env',
          api_version=api_version
        )
        
        return res
        
    def create_environment_variable(self, key, value, target, api_version='v4'):
        # validate target

        res = cls.make_request(
          method='POST',
          resource=f'/projects/{self.id}/env',
          data={
            'key': key,
            'value': value,
            'target': target
          }
        )
        
        return EnvironmentVariable.from_data(self.id, res)
        
    def add_domain(self, domain, redirect=None, api_version='v1'):

        res = cls.make_request(
          method='POST',
          resource=f'/projects/{self.id}/alias'
        )
        
        return
        
    def redirect_domain(self, domain, redirect=None, api_version='v1'):

        res = cls.make_request(
          method='PATCH',
          resource=f'/projects/{self.id}/alias'
        )
        
        return
        
    def remove_domain(self, domain, api_version='v1'):

        res = cls.make_request(
          method='DELETE',
          resource=f'/projects/{self.id}/alias',
          params={
            'domain': domain
          }
        )
        
        return