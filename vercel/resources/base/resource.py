class Resource:
    @classmethod
    def class_url(cls):
      return f'/{cls.RESOURCE_NAME}'