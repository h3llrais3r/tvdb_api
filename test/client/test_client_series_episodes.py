# coding: utf-8

import unittest

from tvdb_api.client import TvdbClient
from tvdb_api.models.episode import Episode
from tvdb_api.models.series_episodes import SeriesEpisodes
from tvdb_api.models.series_episodes_query import SeriesEpisodesQuery
from tvdb_api.models.series_episodes_summary import SeriesEpisodesSummary
from tvdb_api.rest import ApiException


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
        self.assertTrue(response.aired_episodes == '53')
        self.assertIsNotNone(response.aired_seasons)
        self.assertIsInstance(response.aired_seasons, list)
        self.assertTrue(len(response.aired_seasons) == 4)

    def test_get_series_episodes_summary_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_summary(296295)
        self.assertTrue(e.exception.status == 401)

    @unittest.skip('Skipping because no 404 is returned anymore as api response for an invalid series id')
    def test_get_series_episodes_summary_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_summary(0)
        self.assertTrue(e.exception.status == 404)

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

    def test_get_series_episodes_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes(0)
        self.assertTrue(e.exception.status == 404)

    def test_get_series_episodes_by_season(self):
        response = self.client.get_series_episodes_by_season(296295, '1')
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
            self.client.get_series_episodes_by_season(296295, '0')
        self.assertTrue(e.exception.status == 401)

    def test_get_series_episodes_by_season_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episodes_by_season(0, '0')
        self.assertTrue(e.exception.status == 404)

    def test_get_series_episode(self):
        response = self.client.get_series_episode(296295, '1', '1')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].aired_season == 1)
        self.assertTrue(response.data[0].aired_episode_number == 1)

    @unittest.skip('Skipping because no errors are returned anymore in api response')
    def test_get_series_episode_with_errors(self):
        response = self.client.get_series_episode(296295, '1', '1', language='nl')
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
            self.client.get_series_episode(296295, '1', '1')
        self.assertTrue(e.exception.status == 401)

    def test_get_series_episode_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episode(0, '0', '0')
        self.assertTrue(e.exception.status == 404)

    def test_get_series_episode_by_absolute_number(self):
        response = self.client.get_series_episode_by_absolute_number(296295, '1')
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, SeriesEpisodesQuery)
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0].id == 5255064)
        self.assertTrue(response.data[0].absolute_number == 1)

    @unittest.skip('Skipping because no errors are returned anymore in api response')
    def test_get_series_episode_by_absolute_number_with_errors(self):
        response = self.client.get_series_episode_by_absolute_number(296295, '1', language='nl')
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
            self.client.get_series_episode_by_absolute_number(296295, '1')
        self.assertTrue(e.exception.status == 401)

    def test_get_series_episode_by_absolute_number_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_series_episode_by_absolute_number(0, '0')
        self.assertTrue(e.exception.status == 404)


if __name__ == '__main__':
    unittest.main()
