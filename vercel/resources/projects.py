from vercel.resources.base import Resource
class EnvironmentVariable():
  def delete(self):
    res = cls.make_request(
      method='DELETE'
    )

class Project(Resource):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.aliases = aliases
        self.account_id = account_id

    @classmethod
    def get(cls, identifier):
        res = cls.make_request(
        
        )
        
        production_deployment = target.get('production')
        
        if production_deployment is not None:
          production_deployment = Deployment(
            id=production_deployment['id'],
            aliases=production_deployment['alias'],
            alias_assigned=production_deployment['aliasAssigned'],
            created_at=production_deployment['createdAt'],
            created_in=production_deployment['createdIn'],
            deployment_host ame=production_deployment['deploymentHostname'],
            forced=production_deployment['forced'],
            meta=production_deployment['meta'],
            plan=production_deployment['plan'],
            private=production_deployment['private'],
            ready_state=production_deployment['readyState'],
            requested_at=production_deployment['requestedAt'],
            target=production_deployment['target'],
            team_id=production_deployment['teamId'],
            type=production_deployment['type'],
            url=production_deployment['url'],
            user_id=production_deployment['userId']
          )
        
        aliases = [
          Alias(
            domain=alias['domain'],
            target=alias['target'],
            created_at=res['createdAt'],
            configured_by=res['configuredBy'],
            configure_changed_by=res['configureChangedBy']
          )
          for alias in res['alias']
        ]
        
        env = [
          Env(
            key=variable['key'],
            value=variable['value'],
            configuration_id=variable['configurationId'],
            updated_at=variable['updatedAt'],
            created_at=variable['createdAt']
          )
          for variable in res['env']
        ]
        
        latest_deployments = [
          Deployment(
            id=deployment['id'],
            aliases=deployment['alias'],
            alias_assigned=deployment['aliasAssigned'],
            created_at=deployment['createdAt'],
            created_in=deployment['createdIn'],
            deployment_host ame=deployment['deploymentHostname'],
            forced=deployment['forced'],
            meta=deployment['meta'],
            plan=deployment['plan'],
            private=deployment['private'],
            ready_state=deployment['readyState'],
            requested_at=deployment['requestedAt'],
            target=deployment['target'],
            team_id=deployment['teamId'],
            type=deployment['type'],
            url=deployment['url'],
            user_id=deployment['userId']
          )
          for deployment in res['latestDeployments']
        ]

        return cls(
            id=res['id'],
            name=name,
            aliases=aliases,
            account_id=res['accountId'],
            updated_at=res['updatedAt'],
            created_at=res['createdAt'],
            latest_deployments=latest_deployments,
            production_deployment=production_deployment,
            env=env
        )
        
    @classmethod
    def create(cls, name):
        res = cls.make_request(
        
        )
        
        aliases = [
          Alias(
            domain=alias['domain'],
            target=alias['target'],
            created_at=res['createdAt'],
            configured_by=res['configuredBy'],
            configure_changed_by=res['configureChangedBy']
          )
          for alias in res['alias']
        ]

        return cls(
            id=res['id'],
            name=name,
            aliases=aliases,
            account_id=res['accountId'],
            updated_at=res['updatedAt'],
            created_at=res['createdAt']
        )
        
    def update(self, framework=None, public_source=None, build_command=None, dev_command=None, output_directory=None, root_directory=None, api_version='v2'):
        res = cls.make_request(
          method='PATCH',
          resource=f'/projects/{self.id}',
          data={}
        )
        
        self.refresh_from_data(res)
        
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
        
        return Env.create_from_data(self.id, res)
        
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