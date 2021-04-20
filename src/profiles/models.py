from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return {self.email.__str__()}
