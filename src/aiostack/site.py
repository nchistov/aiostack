from . import Item
from . import _base_client
from ._raw_response_dict import RawResponseDict


class Site:
    def __init__(self, name: str, access_token: str | None = None, app_key: str | None = None):
        self.name = name
        self.access_token = access_token
        self.app_key = app_key

    async def get(self, query: str, **kwargs) -> RawResponseDict:
        params = {'site': self.name}
        if self.access_token:
            params['access_token'] = self.access_token
        if self.app_key:
            params['app_key'] = self.app_key
        params.update(kwargs)

        return await _base_client.get(query, **params)

    async def get_all_answers(self, **kwargs) -> list[Item]:
        data = await self.get('answers/', **kwargs)

        return data.items

    async def get_answers_by_id(self, ids: list[int], **kwargs) -> list[Item]:
        url = 'answers/' + ';'.join([str(id) for id in ids])
        data = await self.get(url, **kwargs)

        return data.items

    async def get_comments_on_answers(self, ids: list[int], **kwargs) -> list[Item]:
        url = 'answers/' + ';'.join([str(id) for id in ids]) + '/comments'
        data = await self.get(url, **kwargs)

        return data.items

    async def get_questions_by_answers(self, ids: list[int], **kwargs) -> list[Item]:
        url = 'answers/' + ';'.join([str(id) for id in ids]) + '/questions'
        data = await self.get(url, **kwargs)

        return data.items
