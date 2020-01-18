"""Worker tests api."""
from prosapient.worker import Parser
from unittest.mock import MagicMock
import unittest
from prosapient import config


class TestParser(unittest.TestCase):
    """Test parser api."""

    def setUp(self) -> None:
        """Init dependency."""
        self.logger = MagicMock()
        self.engine = MagicMock()
        self.conf = config
        self.test_parser = Parser(settings=self.conf, log=self.logger, conn_db=self.engine)

    def tearDown(self):
        """Clean up."""
        del self.logger
        del self.engine
        del self.conf
        del self.test_parser

    def test_auth(self):
        """Test auth."""
        res = self.test_parser.auth()
        self.assertTrue(isinstance(res, str))

    def test_handler(self):
        """Handler test."""
        res = self.test_parser.handler()
        self.assertTrue(isinstance(res, dict))

    def test_tags(self):
        """Hashtags test."""
        items = {
            'entities': {
                'hashtags': []
            }
        }
        res = self.test_parser.tags(item=items)
        self.assertEqual(res, '')

    def test_tags_with_items(self):
        """Test tags items."""
        items = {
            'entities': {
                'hashtags': [{'text': 'Text'}]
            }
        }
        res = self.test_parser.tags(item=items)
        self.assertEqual(res, 'Text')

    def test_tags_with_many_items(self):
        """"Test many tags items."""
        items = {
            'entities': {
                'hashtags': [{'text': 'Text1'}, {'text': 'Text2'}]
            }
        }
        res = self.test_parser.tags(item=items)
        self.assertEqual(res, 'Text1,Text2')

    def test_process(self):
        """Test process."""
        self.test_parser.process()
