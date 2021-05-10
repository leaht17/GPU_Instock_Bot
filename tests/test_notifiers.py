import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('ScrapeQueryNotifierMicroservice\scrape_query_notify.py')))
from scrape_query_notify import *
from twilio.rest import Client

""" Tests the functionality of the notification systems, including querying. """

class TestScraper(unittest.TestCase):

    def setUp(self):
        # account sid: AC9d5de46a73c27da46f9c0de98f668e20
        # auth token: 0000ab4bffd746f96c75e19fe9a52079
        # test account sid: AC56538a2f99e2863f36cdea0143417e2c
        # test token: 2ffe0243e02fbaf672773e32dd260ccc 

        # Twilio client set up using live credentials (since testing functionality is limited)
        self.client = Client('AC9d5de46a73c27da46f9c0de98f668e20', '0000ab4bffd746f96c75e19fe9a52079')

    # TODO: add tests for email notifications after implementation is done
    """ Tests if sends correct email message. """
    def test_email_send_message(self):
        print("test_email_send_message not yet implemented")

    # note that this test actually sends a text, using our live credentials
    """ Tests if sends correct text message. """
    def test_send_text(self):
        trial_message = "Sent from your Twilio trial account - "
        url = "Test_GPU_Instock_Bot_URL"
        stock_message = "Message successfully sent for test_notifiers.test_send_text."
        phone_number = '2068593002' # current set to Leah's number for testing
        # phone_number = '5005550006' # valid Twilio magic number (doesn't work with live credentials)

        expected = trial_message + stock_message + "\n\n" + url

    #     send_text(url, stock_message, self.client, phone_number, sender_phone_num='+16782632233')
    #     messages = self.client.messages.list()
    #     print("body: " + messages[0].body)
    #     result = messages[0].body

    #     self.assertEqual(result, expected)

    """ Tests if exception raised when given invalid number. """
    def test_send_text_invalid_number(self):
        trial_message = "Sent from your Twilio trial account - "
        url = "Test_GPU_Instock_Bot_URL"
        stock_message = "Message successfully sent for test_notifiers.test_send_text."
        invalid_phone_number = '5005550001' # invalid magic number

        # uses testing credentials
        self.assertRaises(twilio.base.exceptions.TwilioRestException, \
            send_text, url, stock_message, self.client, invalid_phone_number)
        
    # note: query_module() error - could not connect to server
    def test_query_module(self):
        """ Tests if retrieves correct emails/phone numbers from database. """
        # list_of_emails, list_of_phone_numbers = query_module("fake_url")
    #     self.assertEqual(list_of_emails, [])
    #     self.assertEqual(list_of_phone_numbers, [])

if __name__ == '__main__':
    unittest.main()