# coding: utf-8

import unittest

from tvdb_api_v2.client import TvdbClient
from tvdb_api_v2.models.series_data import SeriesData
from tvdb_api_v2.rest import ApiException


class TestClientSeries(unittest.TestCase):
    """Client series unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.client.login()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_series(self):
        response = self.client.get_series(296295)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesData)
        self.assertTrue(response.data.imdb_id == 'tt4189022')
        self.assertTrue(response.data.series_name == 'Ash vs Evil Dead')

    def test_get_series_with_errors(self):
        response = self.client.get_series(296295, language='nl')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesData)
        self.assertTrue(response.data.imdb_id == 'tt4189022')
        self.assertIsNotNone(response.errors)
        self.assertIsNotNone(response.errors.invalid_language)

    def test_get_series_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series(296295)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series(0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
