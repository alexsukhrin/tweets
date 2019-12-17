from prosapient.worker import Parser
from unittest.mock import MagicMock
import unittest
from prosapient import config


class TestParser(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = MagicMock()
        self.engine = MagicMock()
        self.conf = config
        self.test_parser = Parser(settings=self.conf, log=self.logger, conn_db=self.engine)

    def test_db_property(self):
        res = self.test_parser.db
        self.assertTrue(res)

    def test_auth(self):
        res = self.test_parser.auth()
        self.assertTrue(isinstance(res, str))

    def test_handler(self):
        res = self.test_parser.handler()
        self.assertTrue(isinstance(res, dict))

    def test_tags(self):
        items = {
            'entities': {
                'hashtags': []
            }
        }
        res = self.test_parser.tags(item=items)
        self.assertEquals(res, '')

    def test_tags_with_items(self):
        items = {
            'entities': {
                'hashtags': [{'text': 'Text'}]
            }
        }
        res = self.test_parser.tags(item=items)
        self.assertEquals(res, 'Text')

    def test_tags_with_many_items(self):
        items = {
            'entities': {
                'hashtags': [{'text': 'Text1'}, {'text': 'Text2'}]
            }
        }
        res = self.test_parser.tags(item=items)
        self.assertEquals(res, 'Text1,Text2')

    def test_process(self):
        self.test_parser.process()
