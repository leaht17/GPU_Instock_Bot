import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('GPU_Scrapers/newegg_scraper_bot.py')))
from newegg_scraper_bot import *

""" Tests the functionality of the backend scrapers. """

class TestScraper(unittest.TestCase):

    """ Tests for expected response from is_valid_url. """
    def test_is_valid_url(self):
        input = is_valid_url(200)
        expected = True
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()