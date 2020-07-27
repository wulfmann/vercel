from vercel.resources.base import Resource
from vercel.resources.dns import DnsRecord

class Price(Resource):
  def __init__(self, name, price, period):
    self.name = name
    self.price = price
    self.period = period

  @classmethod
  def from_data(cls, name, data):
    return cls(
      name=name,
      price=data['price'],
      period=data['period']
    )

  def purchase(self, api_version='v4'):
    return Domain.purchase(
      name=self.name,
      expected_price=self.price
    )

class Creator:
  def __init__(self, id, username, email):
    self.id = id
    self.username = username
    self.email = email
    
  @classmethod
  def from_data(cls, data):
    return cls(
      id=data['id'],
      username=data['username'],
      email=data['email']
    )

class Domain(Resource):
    def __init__(self, name, id, service_type, ns_verified_at, txt_verified_at, cdn_enabled, created_at, bought_at, transferred_at, verification_record, verified, nameservers, intended_nameservers, creator, suffix, aliases, certs):
        self.name = name
        self.id = id
        self.service_type = service_type
        self.ns_verified_at = ns_verified_at
        self.txt_verified_at = txt_verified_at
        self.cdn_enabled = cdn_enabled
        self.created_at = created_at
        self.bought_at = bought_at
        self.transferred_at = transferred_at
        self.verification_record = verification_record
        self.verified = verified
        self.nameservers = nameservers
        self.intended_nameservers = intended_nameservers
        self.creator = creator
        self.suffix = suffix
        self.aliases = aliases
        self.certs = certs
        
    @classmethod
    def from_data(cls, data):
      if not 'domain' in data:
        raise ValueError('unabled to pull domain block from data')
      data = data['domain']
      creator = data.get('creator')
      
      if creator is not None:
        creator = Creator.from_data(creator)

      return cls(
        name=data.get('name'),
        id=data.get('id'),
        service_type=data.get('serviceType'),
        ns_verified_at=data.get('nsVerifiedAt'),
        txt_verified_at=data.get('txtVerifiedAt'),
        cdn_enabled=data.get('cdnEnabled'),
        created_at=data.get('createdAt'),
        bought_at=data.get('boughtAt'),
        transferred_at=data.get('transferredAt'),
        verification_record=data.get('verificationRecord'),
        verified=data.get('verified'),
        nameservers=data.get('nameservers', []),
        intended_nameservers=data.get('intendedNameservers', []),
        creator=creator,
        suffix=data.get('suffix'),
        aliases=data.get('aliases', []),
        certs=data.get('certs', [])
      )

    @classmethod
    def get(cls, name, api_version='v4'):
      res = cls.make_request(
        method='GET',
        resource=f'/domains/{name}',
        api_version=api_version
      )
      
      return cls.from_data(res)
      
    @classmethod
    def create(cls, name, api_version='v4'):
      res = cls.make_request(
        method='POST',
        resource=f'/domains',
        data={
          'name': name
        },
        api_version=api_version
      )
      
      return cls.from_data(res)

    @classmethod
    def check_availability(cls, name, api_version='v4'):
      res = cls.make_request(
        method='GET',
        resource=f'/domains/status',
        query_string={
          'name': name
        },
        api_version=api_version
      )
      
      return res

    @classmethod
    def check_price(cls, name, api_version='v4'):
      res = cls.make_request(
        method='GET',
        resource=f'/domains/price',
        query_string={
          'name': name
        },
        api_version=api_version
      )
      
      return Price.from_data(name, res)

    @classmethod
    def purchase(cls, name, expected_price, api_version='v4'):
      res = cls.make_request(
        method='POST',
        resource=f'/domains/buy',
        data={
          'name': name,
          'expectedPrice': expected_price
        },
        api_version=api_version
      )

      return res

    def delete(self, api_version='v4'):
      return self.make_request(
        method='DELETE',
        resource=f'/domains/{self.name}',
        api_version=api_version
      )

    def create_dns_record(self, name, type, value, ttl=None):
        return DnsRecord.create(
            domain_name=self.name,
            name=name,
            type=type,
            value=value,
            ttl=ttl
        )

    def get_dns_record(self, record_id):
        return DnsRecord.get(
            domain_name=self.name,
            record_id=record_id
        )
