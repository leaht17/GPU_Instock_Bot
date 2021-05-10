from django.db import models


# Create your models here.
from django.db.models import PROTECT


# add alias, describe fields
# subscription (row) : user, gpu
#  if subscribe multiple has multiple rows
# subscribers info
# GPU info
class GPU(models.Model):
    url = models.URLField(max_length=512, unique=True)
    alias = models.CharField(max_length=512, unique=True)
    # manufacturer = models.CharField(max_length=256)
    # model = models.CharField(max_length=256)
    # brand = models.CharField(max_length=256)
    gpu_subscription = models.ForeignKey('subscriptions.Subscription', on_delete=PROTECT, blank=True, null=True)

    def getURL(self):
        return self.url

    def getAlias(self):
        return self.alias

    def __str__(self):
        return self.alias

