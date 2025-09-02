class MockResponse:
    def __init__(self, json, status):
        self.data = json
        self.status = status

    async def json(self):
        return self.data

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self
