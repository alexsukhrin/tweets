"""Database queries. """


async def get_tweets(conn, limit: int, offset: int) -> list:
    """The func return tweets from db. """
    sql = "select tw.tweet_id as id, tw.published_at, tw.phrase," \
          " tw.hashtags, tw.author_id, tw.query_phrases " \
          f"from tweets as tw order by tw.published_at limit {limit} offset {offset};"
    return await conn.fetch(sql)


async def get_amount(conn):
    """The func return amount tweets from db. """
    sql = f"select count(*) as amount from tweets;"
    return await conn.fetch(sql)


async def get_hashtags(conn, limit: int):
    """The func return top hashtags from users. """
    sql = f"select hashtags, count(hashtags) as count_hashtags " \
          f"from tweets t where hashtags != ''" \
          f" group by hashtags order by count_hashtags desc limit {limit};"
    return await conn.fetch(sql)


async def get_users(conn, limit: int):
    """The func return top users from tweets. """
    sql = f"select author_id, count(*) as count_tweets from tweets t " \
          f"group by author_id order by count_tweets desc limit {limit};"
    return await conn.fetch(sql)
