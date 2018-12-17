# coding: utf-8

import unittest

from tvdb_api_v2.utils.artwork import get_artwork_url


class TestUtilsArtwork(unittest.TestCase):
    """Utils artwork unit tests."""

    def test_get_artwork_url(self):
        file_name = 'posters/296295-2.jpg'
        thumbnail_file_name = '_cache/posters/296295-2.jpg'
        # asserts
        self.assertTrue('https://www.thetvdb.com/banners/posters/296295-2.jpg', get_artwork_url(file_name))
        self.assertTrue('https://www.thetvdb.com/banners/_cache/posters/296295-2.jpg',
                        get_artwork_url(file_name, thumbnail=True))
        self.assertTrue('https://www.thetvdb.com/banners/_cache/posters/296295-2.jpg',
                        get_artwork_url(thumbnail_file_name))
        self.assertTrue('https://www.thetvdb.com/banners/_cache/posters/296295-2.jpg',
                        get_artwork_url(thumbnail_file_name, thumbnail=True))


if __name__ == '__main__':
    unittest.main()
