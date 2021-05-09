import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('GPU_Scrapers/best_buy_scraper_bot')))
from best_buy_scraper_bot import *

IN_STOCK_PAGE = os.path.join(os.path.dirname('tests/best_buy_gpu_in_stock'), 'best_buy_gpu_in_stock.html')
OUT_OF_STOCK_PAGE = os.path.join(os.path.dirname('tests/best_buy_gpu_sold_out'), 'best_buy_gpu_sold_out.html')

""" Tests the functionality of the best buy scrapers. """

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.testfile_in_stock =  open(IN_STOCK_PAGE)
        self.testdata_in_stock = self.testfile_in_stock.read()

        self.testfile_out_stock = open(OUT_OF_STOCK_PAGE, encoding="utf8")
        self.testdata_out_stock = self.testfile_out_stock.read()

    def tearDown(self):
       self.testfile_in_stock.close()
       self.testfile_out_stock.close()

    """ Tests for expected response from is_valid_url. """
    def test_is_valid_url(self):
        input = is_valid_url(200)
        expected = True
        self.assertEqual(input, expected)

    """ Tests to see that a webpage has GPU in stock """
    def test_page_has_GPU(self):
        input = check_item_in_stock(self.testdata_in_stock)
        expected = True
        self.assertEqual(input, expected)

    """ Tests to see that a webpage does not have a gpu in stock"""
    def test_page_has_no_GPU(self):
        input = check_item_in_stock(self.testdata_out_stock)
        expected = False
        self.assertEqual(input, expected)



if __name__ == '__main__':
    unittest.main()