import aiohttp
from ._raw_response_dict import RawResponseDict
from .errors import HTTPError

BASE_URL = 'https://api.stackexchange.com/2.3/'


async def get(url: str, **kwargs: str | int) -> RawResponseDict:
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + url, params={k: str(v) for k, v in kwargs.items()}) as response:
            data = await response.json()
            status = response.status

            if status != 200:
                raise HTTPError(data['error_message'])

            response = RawResponseDict(**data)
            return response
