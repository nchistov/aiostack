import pytest
import aiostack

from . import MockResponse

resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_get_all_badges(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_badges()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/badges',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_all_non_tag_badges(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_non_tag_badges()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/badges/name',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_badges_by_id(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_badges_by_id([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/badges/1;2',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_badges_recipients(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_badges_recipients()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/badges/recipients',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_badges_recipients_by_id(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_badges_recipients_by_id([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/badges/1;2/recipients',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_all_tag_badges(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_tag_badges()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/badges/tags',
                                                                            params={'site': 'stackoverflow'})
