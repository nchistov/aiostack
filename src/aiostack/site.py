from . import Item
from . import _base_client
from ._raw_response_dict import RawResponseDict


class Site:
    def __init__(self, name: str, access_token: str | None = None, app_key: str | None = None):
        self.name = name
        self.access_token = access_token
        self.app_key = app_key

    async def get(self, query: str, **kwargs: str | int) -> RawResponseDict:
        """Raw get method to api"""
        params = {'site': self.name}
        if self.access_token:
            params['access_token'] = self.access_token
        if self.app_key:
            params['app_key'] = self.app_key
        params.update(kwargs)

        return await _base_client.get(query, **params)

    async def get_info(self) -> Item:
        """Returns a collection of statistics about the site"""
        data = await self.get('info')

        return data.items[0]

    async def get_all_answers(self, **kwargs: str | int) -> list[Item]:
        """Get all answers on the site"""
        data = await self.get('answers', **kwargs)

        return data.items

    async def get_answers_by_id(self, ids: list[int], **kwargs: str | int) -> list[Item]:
        """Get answers identified by a set of ids"""
        url = 'answers' + ';'.join([str(id) for id in ids])
        data = await self.get(url, **kwargs)

        return data.items

    async def get_comments_on_answers(self, ids: list[int], **kwargs: str | int) -> list[Item]:
        """Get comments on the answers identified by a set of ids"""
        url = 'answers/' + ';'.join([str(id) for id in ids]) + '/comments'
        data = await self.get(url, **kwargs)

        return data.items

    async def get_questions_by_answers(self, ids: list[int], **kwargs: str | int) -> list[Item]:
        """Gets all questions the answers identified by ids are on"""
        url = 'answers/' + ';'.join([str(id) for id in ids]) + '/questions'
        data = await self.get(url, **kwargs)

        return data.items

    async def get_all_badges(self, **kwargs: str | int) -> list[Item]:
        """Get all badges on the site, in alphabetical order"""
        data = await self.get('badges', **kwargs)

        return data.items

    async def get_all_non_tag_badges(self, **kwargs: int | str) -> list[Item]:
        """Get all non-tagged-based badges in alphabetical order"""
        data = await self.get('badges/name', **kwargs)

        return data.items

    async def get_badges_by_id(self, ids: list[int], **kwargs: str | int) -> list[Item]:
        """Get the badges identified by ids"""
        url = 'badges/' + ';'.join([str(id) for id in ids])
        data = await self.get(url, **kwargs)

        return data.items

    async def get_badges_recipients(self, **kwargs: int | str):
        """Get badges recently awarded on the site"""
        data = await self.get('badges/recipients', **kwargs)

        return data.items

    async def get_badges_recipients_by_id(self, ids: list[int], **kwargs: int | str) -> list[Item]:
        """Returns recently awarded badges in the system, constrained to a certain set of badges"""
        url = 'badges/' + ';'.join([str(id) for id in ids]) + '/recipients'
        data = await self.get(url, **kwargs)

        return data.items

    async def get_all_tag_badges(self, **kwargs: int | str) -> list[Item]:
        """Returns the badges that are awarded for participation in specific tags"""
        data = await self.get('badges/tags', **kwargs)

        return data.items
