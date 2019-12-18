"""Request handler API """
from aiocache import cached  # type: ignore

try:
    from .query import (
        get_tweets,
        get_amount,
        get_hashtags,
        get_users,
    )
except ImportError:  # pragma: no cover
    from query import (
        get_tweets,
        get_amount,
        get_hashtags,
        get_users,
    )


class ApiHandler:
    """Basic handler api. """
    __slots__ = 'app', 'pool'

    def __init__(self, app):
        self.app = app
        self.pool = self.app.pool

    @cached(key='ApiHandler:tweets', ttl=60)
    async def tweets(self, limit: int, offset: int) -> list:
        """The func return tweets. """
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_tweets(conn=conn, limit=limit, offset=offset)]

    @cached(key='ApiHandler:amount', ttl=60)
    async def amount(self) -> list:
        """The func return amount."""
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_amount(conn=conn)]

    @cached(key='ApiHandler:hashtags', ttl=60)
    async def hashtags(self, limit: int) -> list:
        """The func return hashtags."""
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_hashtags(conn=conn, limit=limit)]

    @cached(key='ApiHandler:users', ttl=60)
    async def users(self, limit: int) -> list:
        """The func return tweets."""
        async with self.pool.acquire() as conn:
            return [dict(x) for x in await get_users(conn=conn, limit=limit)]
