class MockResponse:
    def __init__(self, response, status_code=200):
        self.response = response
        self.status_code = status_code

    def json(self):
        return self.response
