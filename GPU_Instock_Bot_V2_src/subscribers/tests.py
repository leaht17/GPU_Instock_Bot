# Create your tests here.
# test 3 models we have (models.py)
# views.py, add tests.py for dashboard (overall module)

from django.test import TestCase
from django.db import models

# from subscribers.models import Subscriber
from .models import Subscriber


class TestSubscriber(TestCase):

    def test_subscriber_uniqueness(self):
        # Create single subscriber
        s1 = Subscriber.objects.create(email="milan@uw.edu", phone="1234567890")

        # Check phone number and email formats
        self.assertEqual(s1.getEmail(), "milan@uw.edu")
        self.assertTrue("@" in s1.getEmail())

        self.assertEqual(s1.getPhone(), "1234567890")
        self.assertEqual(len(s1.getPhone()), 10)
