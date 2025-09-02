import pytest
import aiostack

from mock_response import MockResponse

@pytest.mark.asyncio
async def test_base_client_get(mocker):
    resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)

    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)

    data = await aiostack._base_client.get('answers/1', site='stackoverflow')

    assert len(data.items) == 0

@pytest.mark.asyncio
async def test_error(mocker):
    with pytest.raises(aiostack.errors.HTTPError):
        resp = MockResponse({'error_id': 400,
                             'error_message': 'No site found for name `ghghgh`',
                             'error_name': 'bad_parameter'}, 400)

        mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)
        await aiostack._base_client.get('answers/1', site='ghghgh')
