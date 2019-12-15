from query import get_tweets


class ApiHandler:
    __slots__ = 'app', 'pool'

    def __init__(self, app):
        self.app = app
        self.pool = self.app.pool

    async def response(self):
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_tweets(conn=conn)]
