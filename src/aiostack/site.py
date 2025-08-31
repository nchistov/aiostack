from ._base_client import get

class Site:
    def __init__(self, name: str):
        self.name = name

    async def get(self, query: str, **kwargs):
        params = {'site': self.name}
        params.update(kwargs)

        return await get(query, **params)
