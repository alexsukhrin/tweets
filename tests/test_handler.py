from prosapient.handler import ApiHandler
import pytest
from prosapient.main import app, startup
from starlette.testclient import TestClient

client = TestClient(app=app)


@pytest.mark.asyncio
async def test_tweets():
    await startup()
    handler = ApiHandler(app=app)
    res = await handler.tweets(limit=1, offset=0)
    assert isinstance(res, list)


@pytest.mark.asyncio
async def test_amount():
    await startup()
    handler = ApiHandler(app=app)
    res = await handler.amount()
    assert isinstance(res, list)


@pytest.mark.asyncio
async def test_hashtags():
    await startup()
    handler = ApiHandler(app=app)
    res = await handler.hashtags(limit=1)
    assert isinstance(res, list)


@pytest.mark.asyncio
async def test_users():
    await startup()
    handler = ApiHandler(app=app)
    res = await handler.users(limit=1)
    assert isinstance(res, list)
