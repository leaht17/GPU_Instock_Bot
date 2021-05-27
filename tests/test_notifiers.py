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

    # TODO: add tests for email notifications after implementation is done
    # """ Tests if sends correct email message. """
    # def test_email_send_message(self):
    #     print("test_email_send_message not yet implemented")

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
        subject = "GPU Instock Bot Test Email"
        message_text = "test_email_create_message has been run"
        sent_email = create_email("to", subject, message_text)
        result = base64.urlsafe_b64decode(sent_email['raw']).decode('utf-8')
        expected = ("Content-Type: text/plain; charset=\"us-ascii\"\n"
            "MIME-Version: 1.0\n"
            "Content-Transfer-Encoding: 7bit\n"
            "to: to\n"
            "from: gpuinstockbot@gmail.com\n"
            "subject: GPU Instock Bot Test Email\n"
            "\n"
            "test_email_create_message has been run")
        self.assertEqual(result, expected)


    """ Tests if retrieves correct emails/phone numbers from database. """
    def test_query_module(self):
        list_of_emails, list_of_phone_numbers = query_module("http://www.fake_url.com")
        self.assertEqual(list_of_emails, [])
        self.assertEqual(list_of_phone_numbers, [])

if __name__ == '__main__':
    unittest.main()