import pytest
import aiostack

from mock_response import MockResponse

@pytest.mark.asyncio
async def test_site_get(mocker):
    resp = MockResponse({'items': [{'answer_id': 7}], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)

    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    site = aiostack.Site(aiostack.sites.StackOverflow)
    data = await site.get('answers/7')

    assert data.items[0]['answer_id'] == 7

@pytest.mark.asyncio
async def test_get_answers(mocker):
    resp = MockResponse({'items': [{}, {}, {}], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)

    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)
    print(dir(mocker.Mock))

    site = aiostack.Site(aiostack.sites.StackOverflow)
    data = await site.get_all_answers(page=1, pagesize=10)

    assert len(data) == 3
