from typing import Any

import aiohttp
from ._raw_response_dict import RawResponseDict

BASE_URL = 'https://api.stackexchange.com/2.3/'


async def get(url: str, *args: list[Any]) -> RawResponseDict:
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + url, params=args) as response:
            data = await response.json()

            response = RawResponseDict(data['items'], data['has_more'], data['quota_max'], data['quota_remaining'])
            return response
