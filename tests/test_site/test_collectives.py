import pytest
import aiostack

from . import MockResponse

resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_site_get_collectives(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_collectives()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/collectives',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_collectives_by_slugs(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_collectives_by_slugs(['aws'])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/collectives/aws',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_questions_by_collectives(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_questions_by_collectives(['aws'])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/collectives/aws/questions',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_answers_by_collectives(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_answers_by_collectives(['aws'])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/collectives/aws/answers',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_tags_by_collectives(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_tags_by_collectives(['aws'])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/collectives/aws/tags',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_users_by_collectives(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_users_by_collectives(['aws'])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/collectives/aws/users',
                                                                            params={'site': 'stackoverflow'})

