from django.test import TestCase
from django.db import models
from .models import Subscriber

# Creates Test Subscribers Class
class TestSubscriber(TestCase):
    # Test case to check if subscriber is unique after form is submitted
    def test_subscriber_uniqueness(self):
        # Create single subscriber
        s1 = Subscriber.objects.create(email="milan@uw.edu", phone="1234567890")

        # Check phone number and email formats
        self.assertEqual(s1.getEmail(), "milan@uw.edu")
        self.assertTrue("@" in s1.getEmail())
        self.assertEqual(s1.getPhone(), "1234567890")
        self.assertEqual(len(s1.getPhone()), 10)