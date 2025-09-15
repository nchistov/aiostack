import pytest
import aiostack

from . import MockResponse

resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_site_get_all_questions(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_all_questions()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_questions_by_id(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_questions_by_id([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/1;2',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_anwers_by_questions(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_answers_by_questions([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/1;2/answers',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_comments_on_questions(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_comments_on_questions([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/1;2/comments',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_linked_questions(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_linked_questions([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/1;2/linked',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_related_questions(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_related_questions([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/1;2/related',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_questions_timeline(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_questions_timeline([1, 2])

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/1;2/timeline',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_active_bounties(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_active_bounties()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/featured',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_questions_without_answers(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_questions_without_answers()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/no-answers',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_site_get_unanswered_questions(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    await site.get_unanswered_questions()

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/questions/unanswered',
                                                                            params={'site': 'stackoverflow'})
