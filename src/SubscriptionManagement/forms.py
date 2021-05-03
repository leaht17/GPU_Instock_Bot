from .models import Subscriber
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SubscriberCreationForm(UserCreationForm):
    class Meta:
        model = Subscriber
        fields = ['username', 'email', 'phone',]


class SubscriberChangeForm(UserChangeForm):
    class Meta:
        model = Subscriber
        fields = ['username', 'email', 'phone',]
