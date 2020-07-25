from vercel.request import make_request

class Profile:
  def __init__(self, service, link):
    self.service = service
    self.link = link

class User:
    def __init__(self, uid, email, name, username, avatar, platform_version, billing, bio, website, profiles):
      self.uid = uid
      self.email = email
      self.name = name
      username = username
      avatar = avatar
      platform_version = platform_version
      billing = Billing(**billing)
      self.bio = bio
      self.website = website
      self.profiles = profiles
    
    @classmethod
    def get(cls):
        user = make_request(
            method='GET',
            resource='/www/user'
        )
        profiles = [
          Profile(
            service=p['service'],
            link=p['link']
          )
          for p in user.get('profiles')
        ]
        return cls(
            uid=user['uid']
        )