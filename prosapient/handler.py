from aiocache import cached

from query import (
    get_tweets,
    get_amount,
    get_hashtags,
    get_users,
)


class ApiHandler:
    __slots__ = 'app', 'pool'

    def __init__(self, app):
        self.app = app
        self.pool = self.app.pool

    @cached(key='ApiHandler:tweets', ttl=60)
    async def tweets(self, limit, offset):
        """
        The func return tweets.
        :param limit: int
        :param offset: int
        :return: list
        """
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_tweets(conn=conn, limit=limit, offset=offset)]

    @cached(key='ApiHandler:amount', ttl=60)
    async def amount(self):
        """The func return amount."""
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_amount(conn=conn)]

    @cached(key='ApiHandler:hashtags', ttl=60)
    async def hashtags(self, limit: int):
        """The func return hashtags."""
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_hashtags(conn=conn, limit=limit)]

    @cached(key='ApiHandler:users', ttl=60)
    async def users(self, limit: int):
        """The func return tweets."""
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_users(conn=conn, limit=limit)]
