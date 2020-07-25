from vercel.request import make_request

class DnsRecord:
    def __init__(self, uid, domain_name):
        self.uid = uid
        self.domain_name = domain_name

    @classmethod
    def create(cls, domain_name, name, type, value, ttl=60):
        res = make_request(
            method='POST',
            resource=f'/v2/domains/{domain_name}/records',
            data={
                'name': name,
                'type': type,
                'value': value,
                'ttl': ttl
            }
        )

        return cls(
            uid=res['uid'],
            domain_name=domain_name
        )

    @classmethod
    def get(cls, domain_name, record_id):
        return cls(
            uid=record_id,
            domain_name=domain_name
        )

    def delete(self):
        make_request(
            method='DELETE',
            resource=f'/v2/domains/{self.domain_name}/records/{self.uid}'
        )