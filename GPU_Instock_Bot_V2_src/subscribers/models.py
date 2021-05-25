from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from gpus.models import GPU

# Create Subscriber Model by setting email, phone, and GPU mapping after
# user fills out form
# Args:
#   Model: current model to be populated
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)
    gpus = models.ManyToManyField(GPU, through='subscriptions.Subscription')

    # Provides phone of subscriber object
    # Returns: PhoneNumberField of user's phone number
    def getPhone(self):
        return self.phone

    # Provides email of subscriber object
    # Returns: EmailField of user's email
    def getEmail(self):
        return self.email

    # Provides string representation of subscriber object
    # Returns: string including user email and phone number
    def __str__(self):
        return self.email.__str__() + "::" + self.phone.__str__()
