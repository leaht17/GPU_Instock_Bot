from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from gpus.models import GPU


class Subscriber(models.Model):
    email = models.EmailField()
    phone = PhoneNumberField()
    gpus = models.ManyToManyField(GPU, through='subscriptions.Subscription')

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def __str__(self):
        return self.email.__str__() + "::" + self.phone.__str__()
