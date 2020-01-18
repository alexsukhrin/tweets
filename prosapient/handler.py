"""Request handler API."""
from aiocache import cached


from .query import get_tweets, get_amount, get_hashtags, get_users


class ApiHandler:
    """Basic handler api."""

    def __init__(self, pool):
        """Init consturctor."""
        self.pool = pool

    @cached(key='ApiHandler:tweets', ttl=60)
    async def tweets(self, limit: int, offset: int) -> list:
        """Get tweets."""
        async with self.pool.acquire() as conn:
            tweets = await get_tweets(conn=conn, limit=limit, offset=offset)
            return [dict(x) for x in tweets]

    @cached(key='ApiHandler:amount', ttl=60)
    async def amount(self) -> list:
        """Get amount."""
        async with self.pool.acquire() as conn:
            amount = await get_amount(conn=conn)
            return [dict(x) for x in amount]

    @cached(key='ApiHandler:hashtags', ttl=60)
    async def hashtags(self, limit: int) -> list:
        """Get hashtags."""
        async with self.pool.acquire() as conn:
            hashtags = await get_hashtags(conn=conn, limit=limit)
            return [dict(x) for x in hashtags]

    @cached(key='ApiHandler:users', ttl=60)
    async def users(self, limit: int) -> list:
        """Users get tweets."""
        async with self.pool.acquire() as conn:
            users = await get_users(conn=conn, limit=limit)
            return [dict(x) for x in users]
