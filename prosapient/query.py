"""Database queries."""


async def get_tweets(conn, limit: int, offset: int) -> list:
    """Get tweets from db."""
    sql = "select tw.tweet_id as id, tw.published_at, tw.phrase," \
          " tw.hashtags, tw.author_id, tw.query_phrases " \
          "from tweets as tw order by tw.published_at limit %s offset %s;"
    return await conn.fetch(sql, (limit, offset))


async def get_amount(conn):
    """Get amount tweets from db."""
    sql = "select count(*) as amount from tweets;"
    return await conn.fetch(sql)


async def get_hashtags(conn, limit: int):
    """Get top hashtags from users."""
    sql = "select hashtags, count(hashtags) as count_hashtags " \
          "from tweets t where hashtags != ''" \
          " group by hashtags order by count_hashtags desc limit %s;"
    return await conn.fetch(sql, (limit,))


async def get_users(conn, limit: int):
    """Get top users from tweets."""
    sql = "select author_id, count(*) as count_tweets from tweets t " \
          "group by author_id order by count_tweets desc limit %s;"
    return await conn.fetch(sql, (limit,))
