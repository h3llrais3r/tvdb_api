import unittest

from tvdb_api_v2.models.series_search import SeriesSearch
from tvdb_api_v2.models.series_search_data import SeriesSearchData
from tvdb_api_v2.rest import ApiException
from tvdb_api_v2.client import TvdbClient


class TestClientSearch(unittest.TestCase):
    """ Client search unit tests """

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
        self.assertIsInstance(response, SeriesSearch)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 296295)

    def test_search_series_by_name_multiple_results(self):
        response = self.client.search_series_by_name('the americans')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearch)
        self.assertTrue(len(response.data) > 1)

    def test_search_series_by_name_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_name('ash vs evil dead')
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_search_series_by_name_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_name('unexisting series')
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')

    def test_search_series_by_imdb_id(self):
        response = self.client.search_series_by_imdb_id('tt4189022')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesSearchData)
        self.assertTrue(response.id == 296295)

    def test_search_series_by_imdb_id_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_imdb_id('tt4189022')
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_search_series_by_imdb_id_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.search_series_by_imdb_id('tt0000000')
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
