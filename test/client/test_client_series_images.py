# coding: utf-8

import unittest

from tvdb_api.client import TvdbClient
from tvdb_api.models.series_image_query_result import SeriesImageQueryResult
from tvdb_api.models.series_image_query_results import SeriesImageQueryResults
from tvdb_api.models.series_images_count import SeriesImagesCount
from tvdb_api.models.series_images_counts import SeriesImagesCounts
from tvdb_api.rest import ApiException


class TestClientSeriesImages(unittest.TestCase):
    """Client series images unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.client.login()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_series_images_count(self):
        response = self.client.get_series_images_count(296295)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesImagesCounts)
        self.assertIsNotNone(response.data)
        self.assertIsInstance(response.data, SeriesImagesCount)
        self.assertTrue(response.data.fanart > 0)
        self.assertTrue(response.data.poster > 0)
        self.assertTrue(response.data.season > 0)
        self.assertTrue(response.data.series > 0)

    def test_get_series_images_count_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_images_count(296295)
        self.assertTrue(e.exception.status == 401)

    def test_get_series_images_count_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_images_count(0)
        self.assertTrue(e.exception.status == 404)

    def test_get_series_images(self):
        response = self.client.get_series_images(296295, 'poster')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesImageQueryResults)
        self.assertTrue(len(response.data) > 0)
        self.assertIsInstance(response.data[0], SeriesImageQueryResult)
        self.assertTrue(response.data[0].id > 0)
        self.assertTrue(response.data[0].key_type == 'poster')

    def test_get_series_images_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_images(296295)
        self.assertTrue(e.exception.status == 401)

    def test_get_series_images_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_images(0)
        self.assertTrue(e.exception.status == 404)

    def test_get_series_highest_rated_image(self):
        response = self.client.get_series_highest_rated_image(296295)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesImageQueryResult)
        self.assertTrue(response.key_type == 'poster')

    def test_get_series_highest_rated_image_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_highest_rated_image(296295)
        self.assertTrue(e.exception.status == 401)

    def test_get_series_highest_rated_image_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_highest_rated_image(0)
        self.assertTrue(e.exception.status == 404)


if __name__ == '__main__':
    unittest.main()
