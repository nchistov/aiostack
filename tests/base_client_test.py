import pytest

import aiostack

@pytest.mark.asyncio
async def test_base_client_get():
    data = await aiostack._base_client.get('answers/1?order=desc&sort=activity&site=stackoverflow')

    assert len(data.items) == 0
