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
    def create(cls, domain_name, name, type, value, ttl=None, api_version='v2'):
        data = {
            'name': name,
            'type': type,
            'value': value
        }

        if ttl is not None:
            data['ttl'] = ttl

        res = cls.make_request(
            method='POST',
            resource=f"/domains/{domain_name}/records",
            data=data,
            api_version=api_version
        )

        return cls(
            id=res['uid'],
            domain_name=domain_name
        )

    def delete(self, api_version='v2', api_key=None, team_id=None, **params):
        self.make_request(
            method='DELETE',
            resource=f'/domains/{self.domain_name}/records/{self.id}',
            api_version=api_version,
            api_key=api_key,
            team_id=team_id
        )
