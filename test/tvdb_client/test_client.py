import unittest
import json

import tvdb_api_v2
from tvdb_api_v2.models.series_search_data import SeriesSearchData
from tvdb_client import TvdbClient


class TestAuth(unittest.TestCase):
    """ Auth unit test stubs """

    def setUp(self):
        self.client = TvdbClient()
        self.client.authenticate()

    def tearDown(self):
        pass

    def test_authenticate(self):
        # asserts
        self.assertIsNotNone(self.client.configuration.api_key['Authorization'])

    def test_search_series_by_name(self):
        response = self.client.search_series_by_name('ash vs evil dead')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchData)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 296295)

    def test_search_series_by_id(self):
        response = self.client.search_series_by_id('tt4189022')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchData)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 296295)


if __name__ == '__main__':
    unittest.main()
