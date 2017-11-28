import unittest

from tvdb_api_v2.models.series_episodes import SeriesEpisodes
from tvdb_api_v2.rest import ApiException
from tvdb_api_v2.client import TvdbClient


class TestClientSeriesEpisodes(unittest.TestCase):
    """ Client series episodes unit tests """

    def setUp(self):
        self.client = TvdbClient()
        self.client.authenticate()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_series_episodes(self):
        response = self.client.get_series_episodes(296295)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodes)
        self.assertTrue(len(response.data) > 0)

    def test_get_series_episodes_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes(296295)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_episodes_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes(0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
