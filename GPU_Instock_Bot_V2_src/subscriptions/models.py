from django.db import models
from django.db.models import CASCADE

# Contains the info for the subscriber and their subscribed GPUs.
class Subscription(models.Model):
    sub_subscriber = models.ForeignKey('subscribers.Subscriber', on_delete=CASCADE)
    sub_gpu = models.ForeignKey('gpus.GPU', on_delete=CASCADE)

    def __str__(self):
        return self.sub_subscriber.__str__() + "::" + self.sub_gpu.__str__()

    def getSubscriber(self):
        return self.sub_subscriber

    def getGPU(self):
        return self.sub_gpu
