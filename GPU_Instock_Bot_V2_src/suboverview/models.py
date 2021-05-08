from django.db import models
from django.contrib.auth.models import User
from django.forms import forms, ModelForm, ModelChoiceField, CheckboxSelectMultiple
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class GPU(models.Model):
    manufacturer = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.manufacturer


class Subscriber(models.Model):
    email = models.EmailField(primary_key=True)
    phone = PhoneNumberField()
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, default='brand')

    def __str__(self):
        return self.email


class SubscriberCreationForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'phone', 'gpu']
