# coding: utf-8

import unittest

from tvdb_api_v2.client import TvdbClient
from tvdb_api_v2.models.episode import Episode
from tvdb_api_v2.models.series_episodes import SeriesEpisodes
from tvdb_api_v2.models.series_episodes_query import SeriesEpisodesQuery
from tvdb_api_v2.models.series_episodes_summary import SeriesEpisodesSummary
from tvdb_api_v2.rest import ApiException


class TestClientSeriesEpisodes(unittest.TestCase):
    """Client series episodes unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.client.login()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_series_episodes_summary(self):
        response = self.client.get_series_episodes_summary(296295)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesSummary)
        self.assertTrue(response.aired_episodes == '47')
        self.assertIsNotNone(response.aired_seasons)
        self.assertIsInstance(response.aired_seasons, list)
        self.assertTrue(len(response.aired_seasons) == 4)

    def test_get_series_episodes_summary_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_summary(296295)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_episodes_summary_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_summary(0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')

    def test_get_series_episodes(self):
        response = self.client.get_series_episodes(296295)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodes)
        self.assertTrue(len(response.data) > 0)
        self.assertIsNotNone(response.links)
        self.assertIsNotNone(response.links.first)
        self.assertIsNotNone(response.links.last)

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

    def test_get_series_episodes_by_season(self):
        response = self.client.get_series_episodes_by_season(296295, 1)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 10)
        self.assertIsInstance(response.data[0], Episode)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].aired_season == 1)
        self.assertTrue(response.data[0].aired_episode_number == 1)

    def test_get_series_episodes_by_season_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_by_season(296295, 0)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_episodes_by_season_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_by_season(0, 0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')

    def test_get_series_episode(self):
        response = self.client.get_series_episode(296295, season=1, episode=1)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].aired_season == 1)
        self.assertTrue(response.data[0].aired_episode_number == 1)

    def test_get_series_episode_with_errors(self):
        response = self.client.get_series_episode(296295, season=1, episode=1, language='nl')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].aired_season == 1)
        self.assertTrue(response.data[0].aired_episode_number == 1)
        self.assertIsNotNone(response.errors)
        self.assertIsNotNone(response.errors.invalid_language)

    def test_get_series_episode_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episode(296295, season=1, episode=1)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_episode_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episode(0, season=0, episode=0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')

    def test_get_series_episode_by_absolute_number(self):
        response = self.client.get_series_episode_by_absolute_number(296295, absolute_number=1)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].absolute_number == 1)

    def test_get_series_episode_by_absolute_number_with_errors(self):
        response = self.client.get_series_episode_by_absolute_number(296295, absolute_number=1, language='nl')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].absolute_number == 1)
        self.assertIsNotNone(response.errors)
        self.assertIsNotNone(response.errors.invalid_language)

    def test_get_series_episode_by_absolute_number_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episode_by_absolute_number(296295, absolute_number=1)
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_series_episode_by_absolute_number_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episode_by_absolute_number(0, absolute_number=0)
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
