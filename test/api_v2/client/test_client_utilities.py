import unittest
from tvdb_api_v2.client.tvdb_client import get_artwork_url


class TestClientUtilities(unittest.TestCase):
    """ Client utilities unit tests """

    def test_get_artwork_url(self):
        artwork_file_name = 'posters/296295-2.jpg'
        # asserts
        self.assertTrue('https://www.thetvdb.com/banners/posters/296295-2.jpg', get_artwork_url(artwork_file_name))


if __name__ == '__main__':
    unittest.main()
