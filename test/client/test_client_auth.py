import time
import unittest

from tvdb_api_v2.rest import ApiException
from tvdb_client import TvdbClient


class TestClientAuth(unittest.TestCase):
    """ Client authentication unit tests """

    def setUp(self):
        self.client = TvdbClient()
        self.token = self.client.authenticate()

    def tearDown(self):
        self.client.clear_token()
        self.token = None

    def test_authenticate(self):
        # asserts
        self.assertIsNotNone(self.token)
        self.assertIsNotNone(self.token.token)

    def test_authenticate_401(self):
        # clear api key
        self.client.configuration.api_key['ApiKey'] = ''
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.authenticate()
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_refresh_token(self):
        # sleep before refreshing the token to be sure we get a new one
        time.sleep(2)
        refresh_token = self.client.refresh_token()
        # asserts
        self.assertIsNotNone(refresh_token)
        self.assertIsNotNone(refresh_token.token)
        self.assertNotEquals(self.token.token, refresh_token.token)

    def test_refresh_token_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.refresh_token()
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')


if __name__ == '__main__':
    unittest.main()
