"""Global variables and settings. """
import os

HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', '8000')

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'sapient')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
               f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY', '454aaArVGfr57ZETE4UXkfQR4')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', 'HPbBPW6GvEJRQveY1vncEhB9lmkhkA7uhoeOPWWMiyDLL3J45A')

API_URL = os.getenv('API_URL', 'https://api.twitter.com/oauth2/token')
TWEETS_URL = os.getenv('TWEETS_URL', 'https://api.twitter.com/1.1/search/tweets.json')

TWITTER_COUNT = os.getenv('TWITTER_COUNT', '10')
TWITTER_QUERY = os.getenv('TWITTER_QUERY', 'украина')

SCHEDULE_WORK = os.getenv('SCHEDULE_WORK', '5')
