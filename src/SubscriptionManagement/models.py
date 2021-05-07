from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser


class Subscriber(models.Model):
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        return self.email


# Create your models here.


class GPU(models.Model):
    manufacturer = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)


class SubscriberCreationForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'phone']
