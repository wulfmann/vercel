from vercel.resources.base import Resource

class DnsRecord(Resource):
    def __init__(self, id, domain_name):
        self.id = id
        self.domain_name = domain_name

    @classmethod
    def get(cls, domain_name, record_id):
        return cls(
            id=record_id,
            domain_name=domain_name
        )

    @classmethod
    def create(cls, domain_name, api_key=None, team_id=None, **params):
        api_version = params.get('api_version', 'v2')

        res = cls.make_request(
            method='POST',
            resource=f"/{api_version}/domains/{domain_name}/records",
            data=params,
            api_key=api_key,
            team_id=team_id
        )

        return cls(
            id=res['uid'],
            domain_name=domain_name
        )

    def delete(self, api_key=None, team_id=None, **params):
        api_version = params.get('api_version', 'v2')

        self.make_request(
            method='DELETE',
            resource=f'/{api_version}/domains/{self.domain_name}/records/{self.id}',
            api_key=api_key,
            team_id=team_id
        )
