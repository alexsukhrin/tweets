import requests
from time import sleep
import logging
from sqlalchemy.exc import IntegrityError

import config
from tables import tweets, engine


class Parser:
    __slots__ = 'conf', 'log', 'conn'

    def __init__(self, settings, log, conn_db):
        self.conf = settings
        self.log = log
        self.conn = conn_db

    @property
    def db(self):
        """The func connect to db. """
        return self.conn.connect()

    def auth(self) -> str:
        """The function returns a token after authorization. """
        data = {'grant_type': 'client_credentials'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        response = requests.post(url=self.conf.API_URL, data=data, headers=headers,
                                 auth=(self.conf.TWITTER_CONSUMER_KEY, self.conf.TWITTER_CONSUMER_SECRET)).json()
        self.log.debug(f'return token')

        return response['access_token']

    def handler(self) -> dict:
        """The function returns a response from the server as json. """
        access_token = self.auth()
        headers = {'Authorization': f'Bearer {access_token}'}
        params = {'q': self.conf.TWITTER_QUERY, 'count': self.conf.TWITTER_COUNT}
        response = requests.get(url=self.conf.TWEETS_URL, headers=headers, params=params).json()
        self.log.debug(f'return json response')

        return response

    def tags(self, item: dict) -> str:
        """The function selects hashtags from dict. """
        if len(item['entities']['hashtags']) > 0:
            hashtags = ','.join([i['text'] for i in item['entities']['hashtags']])
            self.log.debug(f'return {hashtags}')
            return hashtags

        return ''

    def process(self) -> None:
        """The function collects and saves tweets to the database. """
        data = self.handler()
        for item in data['statuses']:
            hashtags = self.tags(item)
            tweet = {
                'tweet_id': item['id'],
                'published_at': item['created_at'],
                'phrase': item['text'],
                'hashtags': hashtags,
                'author_id': item['user']['id'],
                'query_phrases': self.conf.TWITTER_QUERY
            }
            try:
                self.db.execute(tweets.insert().values(**tweet))
                self.log.debug('Save tweet', tweet)
            except IntegrityError:
                self.log.debug('Tweet already exists')
            finally:
                self.db.close()


def main(run: bool, timeout: int) -> None:
    """The main function that starts the periodic process of parsing tweet. """
    logging.basicConfig()
    logger = logging.getLogger("proSapient.worker.tweets")
    logger.setLevel(logging.DEBUG)

    while run:
        parser = Parser(settings=config, log=logger, conn_db=engine)
        parser.process()
        sleep(timeout)


if __name__ == '__main__':
    main(run=True, timeout=int(config.SCHEDULE_WORK))
