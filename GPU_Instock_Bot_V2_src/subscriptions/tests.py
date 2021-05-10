from django.test import TestCase
from django.db import models

from subscriptions.models import Subscription
from subscribers.models import Subscriber
from gpus.models import GPU


class SubscriptionTestCase(TestCase):
    def setUpData(cls):
        # Set up gpu and subscriber association with subscription
        curSubscriber = Subscriber.objects.create(email="elin@uw.edu", phone="1234567890")
        curGPU = GPU.object.create(
            url="https://www.bestbuy.com/site/pny-geforce-gt1030-2gb-pci-e-3-0-graphics-card-black/5901353.p?skuId=5901353",
            alias="1")
        curSub = Subscription.objects.create(sub_subscriber=curSubscriber, sub_gpu=curGPU)

        self.assertEqual(curSub.getSubscriber().getEmail(), "elin@uw.edu")

