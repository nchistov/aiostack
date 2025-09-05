import pytest
import aiostack

from . import MockResponse

resp = MockResponse({'items': [], 'has_more': False, 'quota_max': 10000, 'quota_remaining': 9999}, 200)


@pytest.mark.asyncio
async def test_base_client_get(mocker):
    mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=resp)
    await aiostack._base_client.get('answers/1', site='stackoverflow')

    aiostack._base_client.aiohttp.ClientSession.get.assert_called_once_with('https://api.stackexchange.com/2.3/answers/1',
                                                                            params={'site': 'stackoverflow'})


@pytest.mark.asyncio
async def test_error(mocker):
    with pytest.raises(aiostack.errors.HTTPError):
        err_resp = MockResponse({'error_id': 400,
                             'error_message': 'No site found for name `smth`',
                             'error_name': 'bad_parameter'}, 400)

        mocker.patch('aiostack._base_client.aiohttp.ClientSession.get', return_value=err_resp)
        await aiostack._base_client.get('answers/1', site='smth')
