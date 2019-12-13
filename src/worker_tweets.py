import requests
from config import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, API_URL, TWEETS_URL, TWITTER_COUNT, TWITTER_QUERY,\
    SCHEDULE_WORK
from pprint import pprint
from tables import tweets
from tables import engine
from time import sleep
import logging

logging.basicConfig()
logger = logging.getLogger("proSapient.worker.tweets")
logger.setLevel(logging.DEBUG)


def auth():
    data = {'grant_type': 'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    response = requests.post(url=API_URL, data=data, headers=headers,
                             auth=(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)).json()
    return response['access_token']


def handler():
    access_token = auth()
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': TWITTER_QUERY, 'count': TWITTER_COUNT}
    response = requests.get(url=TWEETS_URL, headers=headers, params=params).json()
    return response


def process():
    data = handler()
    conn = engine.connect()
    for item in data['statuses']:
        tweet = {
            'tweet_id': item['created_at'],
            'published_at': item['id'],
            'phrase': item['text'],
            'hashtags': item['entities']['hashtags'],
            'author_id': item['entities']['user_mentions'][0]['id'],
            'query_phrases': TWITTER_QUERY
        }
        pprint(tweet)
        conn.execute(tweets.insert().values(**tweet))
    conn.close()


def main(run=True):
    while run:
        process()
        sleep(int(SCHEDULE_WORK))


if __name__ == '__main__':
    main()
