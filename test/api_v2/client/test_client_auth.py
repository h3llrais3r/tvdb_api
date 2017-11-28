import time
import unittest

from tvdb_api_v2.rest import ApiException
from tvdb_api_v2.client import TvdbClient


class TestClientAuth(unittest.TestCase):
    """ Client authentication unit tests """

    def setUp(self):
        self.client = TvdbClient()
        self.client.authenticate()

    def tearDown(self):
        self.client.clear_token()

    def test_authenticate(self):
        # asserts
        self.assertIsNotNone(self.client.configuration.api_key['Authorization'])

    def test_authenticate_401(self):
        # clear api key
        self.client.configuration.api_key['ApiKey'] = ''
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.authenticate()
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_refresh_token(self):
        # get existing token
        token = self.client.configuration.api_key['Authorization']
        # sleep before refreshing the token to be sure we get a new one
        time.sleep(2)
        self.client.refresh_token()
        new_token = self.client.configuration.api_key['Authorization']
        # asserts
        self.assertIsNotNone(new_token)
        self.assertNotEquals(token, new_token)

    def test_refresh_token_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.refresh_token()
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')


if __name__ == '__main__':
    unittest.main()
