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
    def get_build_logs(cls, deployment_id, limit, since, until, until, direction, version='v2'):
        logs = make_request(
            method='GET',
            resource=f'/{version}/now/deployments/{deployment_id}/events'
        )


        return cls(
        )