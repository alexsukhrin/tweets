"""Unit tests API."""
from prosapient.handler import ApiHandler
import pytest
from prosapient.main import app, startup
from starlette.testclient import TestClient

client = TestClient(app=app)


@pytest.mark.asyncio
async def test_tweets():
    """Test tweets api."""
    await startup()
    handler = ApiHandler(pool=app.pool)
    res = await handler.tweets(limit=1, offset=0)
    assert isinstance(res, list)


@pytest.mark.asyncio
async def test_amount():
    """Test amount api."""
    await startup()
    handler = ApiHandler(pool=app.pool)
    res = await handler.amount()
    assert isinstance(res, list)


@pytest.mark.asyncio
async def test_hashtags():
    """Test hashtags api."""
    await startup()
    handler = ApiHandler(pool=app.pool)
    res = await handler.hashtags(limit=1)
    assert isinstance(res, list)


@pytest.mark.asyncio
async def test_users():
    """Test users api."""
    await startup()
    handler = ApiHandler(pool=app.pool)
    res = await handler.users(limit=1)
    assert isinstance(res, list)
