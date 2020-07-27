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

    def invite_user(self, email, role, api_version='v1'):
      # todo validate role
      return self.make_request(
          method='POST',
          resource=f'/teams/{self.id}/members',
          data={
            'email': email,
            'role': role
          },
          api_version=api_version
      )

    def update_user(self, user_id, role, confirmed=None, api_version='v1'):
      # todo validate role
      data = {
        'role': role
      }

      if confirmed is not None:
        data['confirmed'] = confirmed

      return self.make_request(
          method='PATCH',
          resource=f'/teams/{self.id}/members/{user_id}',
          data=data,
          api_version=api_version
      )


    def request_to_join(self, origin, commit_id=None, repo_id=None, api_version='v1'):
      # todo validate origin
      data = {
        'origin': origin
      }

      if commit_id is not None:
        data['commitId'] = commit_id

      if repo_id is not None:
        data['repoId'] = repo_id

      return self.make_request(
          method='POST',
          resource=f'/teams/{self.id}/request',
          data=data,
          api_version=api_version
      )

    def remove_user(self, user_id, api_version='v1'):
      return self.make_request(
          method='DELETE',
          resource=f'/teams/{self.id}/members/{user_id}',
          api_version=api_version
      )
