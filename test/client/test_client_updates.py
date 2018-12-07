# coding: utf-8

import unittest
from datetime import date, timedelta

from tvdb_api_v2.client import TvdbClient
from tvdb_api_v2.models.update import Update
from tvdb_api_v2.models.update_data import UpdateData
from tvdb_api_v2.rest import ApiException


class TestClientEpisodes(unittest.TestCase):
    """Client updates unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.client.login()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_updates(self):
        day = 24 * 60 * 60
        yesterday = date.today() - timedelta(days=1)
        yesterday_epoch = (yesterday.toordinal() - date(1970, 1, 1).toordinal()) * day
        response = self.client.get_updates(str(yesterday_epoch))
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, UpdateData)
        self.assertTrue(len(response.data) > 0)
        self.assertIsInstance(response.data[0], Update)

    def test_get_episode_401(self):
        self.client.clear_token()
        day = 24 * 60 * 60
        today_epoch = (date.today().toordinal() - date(1970, 1, 1).toordinal()) * day
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_updates(str(today_epoch))
        self.assertTrue(e.exception.status == 401)
        self.assertTrue(e.exception.reason == 'Unauthorized')

    def test_get_episode_404(self):
        # asserts
        day = 24 * 60 * 60
        tomorrow = date.today() + timedelta(days=1)
        tomorrow_epoch = (tomorrow.toordinal() - date(1970, 1, 1).toordinal()) * day
        with self.assertRaises(ApiException) as e:
            self.client.get_updates(str(tomorrow_epoch))
        self.assertTrue(e.exception.status == 404)
        self.assertTrue(e.exception.reason == 'Not Found')


if __name__ == '__main__':
    unittest.main()
