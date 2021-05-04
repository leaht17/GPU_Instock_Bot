from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SubscriberCreationForm, SubscriberChangeForm
from .models import Subscriber, GPU


# Register your models here.

class SubscriberAdmin(UserAdmin):
    add_form = SubscriberCreationForm
    form = SubscriberChangeForm
    model = Subscriber
    list_display = ['username', 'email', 'phone']


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(GPU)
