from starlette.testclient import TestClient
from src.api import app, startup


async def test_tweets_view():
    await startup()
    client = TestClient(app=app)
    res = client.get('/')
    assert res.status_code == 200


async def test_amount_view():
    await startup()
    client = TestClient(app=app)
    res = client.get('/amount')
    assert res.status_code == 200


async def test_hashtags_view():
    await startup()
    client = TestClient(app=app)
    res = client.get('/hashtags')
    assert res.status_code == 200


async def test_users_view():
    await startup()
    client = TestClient(app=app)
    res = client.get('/users')
    assert res.status_code == 200
