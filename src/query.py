from tables import tweets
import databases


async def get_tweets(conn) -> list:
    """
    The func return tweets from db.
    :param conn:
    :return: list
    """
    sql = "select tw.tweet_id as id, tw.published_at, tw.phrase," \
          " tw.hashtags, tw.author_id, tw.query_phrases " \
          "from tweets as tw order by tw.published_at;"
    return await conn.fetch(sql)
