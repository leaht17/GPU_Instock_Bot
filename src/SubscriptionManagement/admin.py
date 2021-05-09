from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Subscriber, GPU, SubscriberCreationForm


# Register your models here.

admin.site.register(Subscriber)
admin.site.register(GPU)
