from vercel.request import make_request

class Billing:
  def __init__(self, plan, period, trial, cancelation, addons):
    self.plan = self.plan
    self.period = period
    self.trial = trial
    self.cancelation = cancelation
    self.addons = addons

class Profile:
  def __init__(self, service, link):
    self.service = service
    self.link = link

class User:
    def __init__(self, uid, email, name, username, avatar, platform_version, billing, bio, website, profiles):
      self.uid = uid
      self.email = email
      self.name = name
      self.username = username
      self.avatar = avatar
      self.platform_version = platform_version
      self.billing = billing
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
          uid=user['uid'],
          email=user['email'],
          name=user['name'],
          username=user['username'],
          avatar=user['avatar'],
          platform_version=user['platformVersion'],
          billing=Billing(**user['billibg']),
          bio=user['bio'],
          website=user['website'],
          profiles=profiles
        )