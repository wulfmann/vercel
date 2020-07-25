from vercel.request import make_request
from vercel.resources.base import CreatableResource

class Record(Resource):
    def __init__(self, uid, domain_name):
        self.uid = uid
        self.domain_name = domain_name

class Domain(
  CreateableResource
):
    RESOURCE_NAME = 'domains'

    def __init__(self): pass

    def create_dns_record(cls, name, type, value, ttl=60, api_version='v2'):
      cls.make_request(
        res = make_request(
            method='POST',
            resource=f'/{api_version}/{cls.class_url()}/{domain_name}/records',
            data={
                'name': name,
                'type': type,
                'value': value,
                'ttl': ttl
            }
        )

        return Record(
            uid=res['uid'],
            domain_name=domain_name
        )

    def get_dns_record(cls, domain_name, record_id):
        return Record(
            uid=record_id,
            domain_name=domain_name
        )

    def delete_dns_record(self):
        make_request(
            method='DELETE',
            resource=f'/v2/domains/{self.domain_name}/records/{self.uid}'
        )