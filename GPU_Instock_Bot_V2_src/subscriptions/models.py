from django.db import models


# Create your models here.
from django.db.models import CASCADE


class Subscription(models.Model):
    sub_subscriber = models.ForeignKey('subscribers.Subscriber', on_delete=CASCADE)
    sub_gpu = models.ForeignKey('gpus.GPU', on_delete=CASCADE)
    
    def getSubscriber(self):
        return self.sub_subscriber

    def getGPU(self):
        return self.sub_gpu
