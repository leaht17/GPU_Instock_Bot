from ScrapeQueryNotifierMicroservice.scrape_query_notify import email_body
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('ScrapeQueryNotifierMicroservice/scrape_query_notify.py')))
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
        self.test_client = Client('AC56538a2f99e2863f36cdea0143417e2c', '2ffe0243e02fbaf672773e32dd260ccc')

    """ Tests if correctly sends text message. """
    def test_send_text(self):
        # note that this test actually sends a text, using our live credentials
        
        trial_message = "Sent from your Twilio trial account - "
        url = "Test_GPU_Instock_Bot_URL"
        stock_message = "Message successfully sent for test_notifiers.test_send_text."
        valid_unavailable_phone_number = '5005550006' # valid, unavailable magic number
        expected = trial_message + stock_message + "\n\n" + url
        
        # expects no error in sending message
        send_text(url, stock_message, self.test_client, valid_unavailable_phone_number)

        # commented out for now because it actually sends text
        # valid_phone_number = '2068593002' # currently set to Leah's number for testing
        # send_text(url, stock_message, self.client, valid_phone_number, sender_phone_num='+16782632233')
        # messages = self.client.messages.list()
        # print("body: " + messages[0].body)
        # result = messages[0].body

        # compares message sent with expected message
        # self.assertEqual(result, expected)

    """ Tests if exception raised when given invalid number. """
    def test_send_text_invalid_number(self):
        trial_message = "Sent from your Twilio trial account - "
        url = "Test_GPU_Instock_Bot_URL"
        stock_message = "Message successfully sent for test_notifiers.test_send_text."
        invalid_phone_number = '5005550001' # invalid magic number

        # uses testing credentials
        self.assertRaises(twilio.base.exceptions.TwilioRestException, \
            send_text, url, stock_message, self.test_client, invalid_phone_number)
        
    """ Tests if creates email message in expected MIMEText format."""
    def test_email_create_message(self):
        gmail_username = "gpuinstockbot@gmail.com"
        recipient_email = "gpuinstockbot@gmail.com"
        stock_message = "test_email_create_message has been run"
        url = "http://www.testurl.com"
        
        result = email_body(gmail_username, recipient_email, stock_message, url)
        message_start_index = 201 + len(gmail_username) + len(recipient_email)
        message = str(result)[message_start_index:-46] # gets html message
        
        expected_message = ("\nContent-Type: text/html; charset=\"us-ascii\"\n"
            "MIME-Version: 1.0\n"
            "Content-Transfer-Encoding: 7bit\n"
            "\n"
            "    <html>\n"
            "        <body>\n"
            "        <p>\n"
            "            Your item has been restocked at BestBuy<br><br>\n"
            "\n"
            "            test_email_create_message has been run<br>\n"
            "\n"
            "            <a href=\"http://www.testurl.com\">http://www.testurl.com</a>\n"
            "        </p>\n"
            "        </body>\n"
            "    </html>\n")
    
        self.assertEqual(result.get("from"), gmail_username)
        self.assertEqual(result.get("to"), recipient_email)
        self.assertEqual(message, expected_message)

    """ Tests if retrieves correct emails/phone numbers from database. """
    def test_query_module(self):
        list_of_emails, list_of_phone_numbers = query_module("http://www.fake_url.com")
        self.assertEqual(list_of_emails, [])
        self.assertEqual(list_of_phone_numbers, [])

if __name__ == '__main__':
    unittest.main()