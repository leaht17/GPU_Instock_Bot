import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('ScrapeQueryNotifierMicroservice/scrape_query_notify')))
from scrape_query_notify import *

class TestScraper(unittest.TestCase):
    
    def setUp(self):
        chromeOptions = Options()
        chromeOptions.headless = headless
        self.browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chromeOptions)
        
        self.in_stock_url = "https://www.bestbuy.com/site/pny-geforce-gt-710-2gb-pci-express-2-0-graphics-card-black/5092306.p?skuId=5092306"
        self.out_stock_url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
        self.not_best_buy_url = "https://youtu.be/dQw4w9WgXcQ"

    def test_page_has_GPU(self):
        success, message = scraper(self.browser, self.in_stock_url)
        expected_success = True
        self.assertEqual(success, expected_success)
        self.assertNotEqual(message, "Null")
    
    def test_page_has_no_GPU(self):
        success, message = scraper(self.browser, self.out_stock_url)
        expected_success = False
        self.assertEqual(success, expected_success)
        self.assertEqual(message, "Null")
    
    def test_on_non_best_buy_page(self):
        success, message = scraper(self.browser, self.not_best_buy_url)
        expected_success = False
        self.assertEqual(success, expected_success)
        self.assertEqual(message, "Null")


