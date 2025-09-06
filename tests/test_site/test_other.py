import pytest
import aiostack

from . import MockResponse

resp = MockResponse({'items': [{}], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_site_info(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_info()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/info',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_privileges(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_privileges()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/privileges',
                                                                            params={'site': 'stackoverflow'})
