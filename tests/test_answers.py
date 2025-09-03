import pytest
import aiostack

from mock_response import MockResponse

resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_site_get(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get('answers/1')

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/answers/1',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_get_all_answers(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_answers(page=1, pagesize=10)

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/answers',
                                                                            params={'page': '1', 'pagesize': '10', 'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_all_answers_by_id(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_answers_by_id([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/answers/1;2',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_comments_on_answers(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_comments_on_answers([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/answers/1;2/comments',
                                                                            params={'site': 'stackoverflow'})

@pytest.mark.asyncio
async def test_get_questions_by_answers(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_questions_by_answers([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/answers/1;2/questions',
                                                                            params={'site': 'stackoverflow'})
