import pytest

import aiostack

@pytest.mark.asyncio
async def test_site_get():
    site = aiostack.Site(aiostack.sites.StackOverflow)
    data = await site.get('answers/7')

    assert data.items[0]['answer_id'] == 7

@pytest.mark.asyncio
async def test_get_answers():
    site = aiostack.Site(aiostack.sites.StackOverflow)
    data = await site.get_all_answers(page=1, pagesize=10)

    assert len(data) == 10
