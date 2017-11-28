import unittest

from tvdb_api_v2.models.episode import Episode
from tvdb_api_v2.rest import ApiException
from tvdb_api_v2.client import TvdbClient


class TestClientEpisodes(unittest.TestCase):
    """ Client episodes unit tests """

    def setUp(self):
        self.client = TvdbClient()
        self.client.authenticate()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_episode(self):
        response = self.client.get_episode(5255064)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Episode)
        self.assertTrue(response.series_id == '296295')
        self.assertTrue(response.aired_season == 1)
        self.assertTrue(response.aired_episode_number == 1)

    def test_get_episode_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_episode(5255064)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_episode_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_episode(0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
