from starlette.testclient import TestClient
from api import app, startup


async def test_tweets_view():
    await startup()
    client = TestClient(app=app)
    res = client.get('/')
    assert res.status_code == 200
