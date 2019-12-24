# coding: utf-8

import time
import unittest

from tvdb_api.client import TvdbClient
from tvdb_api.rest import ApiException


class TestClientAuth(unittest.TestCase):
    """Client authentication unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.token = self.client.login()

    def tearDown(self):
        self.client.clear_token()
        self.token = None

    def test_authenticate(self):
        # asserts
        self.assertIsNotNone(self.token)

    def test_authenticate_401(self):
        # clear api key
        self.client.configuration.api_key['ApiKey'] = ''
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.login()
        self.assertTrue(e.exception.status == 401)

    def test_refresh_token(self):
        # sleep before refreshing the token to be sure we get a new one
        time.sleep(2)
        refresh_token = self.client.refresh_token()
        # asserts
        self.assertIsNotNone(refresh_token)
        self.assertNotEquals(self.token, refresh_token)

    def test_refresh_token_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.refresh_token()
        self.assertTrue(e.exception.status == 401)


if __name__ == '__main__':
    unittest.main()
