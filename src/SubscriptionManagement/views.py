from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SubscriberCreationForm


# Create your views here.


def subscriptionmanager(request):
    return render(request, template_name='index.html')


class SignUpView(generic.CreateView):
    form_class = SubscriberCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
