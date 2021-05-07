import unittest
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath('GPU_Scrapers/newegg_scraper_bot.py')))
# from newegg_scraper_bot import *

""" Tests the functionality of the backend scrapers. """

class TestScraper(unittest.TestCase):

    """ Placeholder test """
    def test_input(self):
        # replace input with user input from website
        input = "email@uw.edu"
        expected = "email@uw.edu"
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()