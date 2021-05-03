from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser


class Subscriber(AbstractUser):
    pass
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        return self.email


# Create your models here.


class GPU(models.Model):
    manufacturer = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)

