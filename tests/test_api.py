from prosapient.main import app, startup
from starlette.testclient import TestClient

client = TestClient(app=app)


async def test_tweets_view():
    await startup()
    res = client.get('/')
    assert res.status_code == 200


async def test_amount_view():
    await startup()
    res = client.get('/amount')
    assert res.status_code == 200


async def test_hashtags_view():
    await startup()
    res = client.get('/hashtags')
    assert res.status_code == 200


async def test_users_view():
    await startup()
    res = client.get('/users')
    assert res.status_code == 200
