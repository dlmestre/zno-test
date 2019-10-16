import unittest
from utils.url import Url, UrlException


class TestUrl(unittest.TestCase):

    def test_defined_url(self):
        url = Url.stringify('url', 2019, 10, 15)
        self.assertEqual(url, 'url/2019/10/15')

    def test_undefined_url(self):
        with self.assertRaises(UrlException):
            url = Url.stringify('', 2019, 10, 15)
