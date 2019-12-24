# coding=utf-8

import unittest

from tvdb_api.client import TvdbClient
from tvdb_api.models.series_search_result import SeriesSearchResult
from tvdb_api.models.series_search_results import SeriesSearchResults
from tvdb_api.rest import ApiException


class TestClientSearch(unittest.TestCase):
    """Client search unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.client.login()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_search_series_by_name(self):
        response = self.client.search_series_by_name('ash vs evil dead')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchResults)
        self.assertTrue(isinstance(response.data, list))
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 296295)

    def test_search_series_by_name_with_special_characters(self):
        response = self.client.search_series_by_name(u'Fais pas ci, fais pas ça'.encode('utf-8'), language='fr')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchResults)
        self.assertTrue(isinstance(response.data, list))
        self.assertTrue(len(response.data) != 0)
        self.assertTrue([x for x in response.data if x.id == 80977])

    def test_search_series_by_name_multiple_results(self):
        response = self.client.search_series_by_name('the americans')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchResults)
        self.assertTrue(isinstance(response.data, list))
        self.assertTrue(len(response.data) > 1)

    def test_search_series_by_name_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_name('ash vs evil dead')
        self.assertTrue(e.exception.status == 401)

    def test_search_series_by_name_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_name('unexistingseries')
        self.assertTrue(e.exception.status == 404)

    def test_search_series_by_imdb_id(self):
        response = self.client.search_series_by_imdb_id('tt4189022')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchResult)
        self.assertTrue(response.id == 296295)

    def test_search_series_by_imdb_id_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_imdb_id('tt4189022')
        self.assertTrue(e.exception.status == 401)

    def test_search_series_by_imdb_id_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_imdb_id('tt0000000')
        self.assertTrue(e.exception.status == 404)


if __name__ == '__main__':
    unittest.main()
