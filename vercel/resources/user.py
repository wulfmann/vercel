from vercel.resources.base import Resource

class User(Resource):
    def __init__(self): pass

    @classmethod
    def from_data(cls, data):
        return cls()

    @classmethod
    def get(cls, api_version=''):
        res = cls.make_request(
            method='GET',
            resource='www/user', # no trailing slash because no api version
            api_version=api_version
        )

        return res
