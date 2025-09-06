import pytest
import aiostack

from . import MockResponse

resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_site_get_all_posts(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_posts()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/posts',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_posts_by_id(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_posts_by_id([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/posts/1;2',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_comments_on_posts(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_comments_on_posts([1,2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/posts/1;2/comments',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_revisions_by_posts(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_revisions_by_posts([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/posts/1;2/revisions',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_edits_by_posts(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_edits_by_posts([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/posts/1;2/suggested-edits',
                                                                            params={'site': 'stackoverflow'})
