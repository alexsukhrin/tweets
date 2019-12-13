import os

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
               f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')

API_URL = os.getenv('API_URL')
TWEETS_URL = os.getenv('TWEETS_URL')

TWITTER_COUNT = os.getenv('TWITTER_COUNT')
TWITTER_QUERY = os.getenv('TWITTER_QUERY')

SCHEDULE_WORK = os.getenv('SCHEDULE_WORK')
