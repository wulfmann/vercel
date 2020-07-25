from vercel.resources.base import Resource
from vercel.resources.dns import DnsRecord

class Domain(Resource):
    def __init__(self, name, api_key=None, team_id=None):
        self.name = name
        self.owner = {
            'api_key': api_key,
            'team_id': team_id
        }

    def create_dns_record(self, **params):
        return DnsRecord.create(
            domain_name=self.name,
            api_key=self.owner['api_key'],
            team_id=self.owner['team_id'],
            **params
        )

    def get_dns_record(self, record_id):
        return DnsRecord(
            id=record_id,
            domain_name=self.name,
            **self.owner
        )
