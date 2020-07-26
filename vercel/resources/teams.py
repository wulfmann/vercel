from vercel.resources.base import Resource

class Team(Resource):
    def __init__(self, id, slug, name, created, creator_id, avatar):
        self.id = id
        self.slug = slug
        self.name = name
        self.created = created
        self.creator_id = creator_id
        self.avatar = avatar

    @classmethod
    def from_data(cls, data):
      return cls(
        id=data['id'],
        slug=data.get('slug'),
        name=data.get('name'),
        created=data.get('created'),
        creator_id=data.get('creatorId'),
        avatar=data.get('avatar')
      )

    @classmethod
    def get(cls, slug=None, id=None, api_version='v1'):
        if slug is None and id is None:
          raise Exception('you can only specify one of name or id')
        if slug is not None and id is not None:
          raise Exception('you must specify one of name or id')
          
        resource = f"/teams"
        params = {}
        
        if slug is not None:
          params['slug'] = slug
          
        if id is not None:
          resource += f'/{id}'

        res = cls.make_request(
            method='GET',
            resource=resource,
            query_string=params,
            api_version=api_version
        )

        return cls.from_data(res)


    @classmethod
    def create(cls, slug, api_version='v1'):
        res = cls.make_request(
            method='POST',
            resource=f"/teams",
            data={
              'slug': slug
            },
            api_version=api_version
        )

        return cls.from_data(res)

    def delete(self, api_version='v1'):
        self.make_request(
            method='DELETE',
            resource=f'/teams/{self.id}',
            api_version=api_version
        )

    def update(self, slug, name, api_version='v1'):
        res = self.make_request(
            method='PATCH',
            resource=f'/teams/{self.id}',
            data={
              'slug': slug,
              'name': name
            },
            api_version=api_version
        )
        # todo refactor this to update current object instead of creating a new one
        return Team.from_data(res)
