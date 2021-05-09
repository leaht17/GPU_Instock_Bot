from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
from .models import SubscriberCreationForm


def subscriptionmanager(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriberCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/GPUInstockBot')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriberCreationForm()
    return render(request, 'index.html', {'form': form})