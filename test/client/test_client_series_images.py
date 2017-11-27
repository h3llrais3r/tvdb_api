import unittest

from tvdb_api_v2.models.series_images_count import SeriesImagesCount
from tvdb_api_v2.models.series_images_counts import SeriesImagesCounts
from tvdb_api_v2.rest import ApiException
from tvdb_client import TvdbClient


class TestClientSeriesImages(unittest.TestCase):
    """ Client series images unit tests """

    def setUp(self):
        self.client = TvdbClient()
        self.client.authenticate()

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
        self.assertTrue(response.data.poster > 0)

    def test_get_series_images_count_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_images_count(296295)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_images_count_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_images_count(0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
