class DeletableResource(Resource):
    @classmethod
    def delete(cls, uid, **params):
        url = f'{cls.class_url()}/{uid}
        return cls.make_request("delete", url, **params)
