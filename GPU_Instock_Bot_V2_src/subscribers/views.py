from django.shortcuts import render
from .forms import SubscriptionForm
from django.http import HttpResponseRedirect
from .models import Subscriber

# Creates Subscription View Class passing in user request from submission
# Args:
#   request: data from form submission on subscription view
def subscriptionview(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = SubscriptionForm(request.POST)

        # Check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriptionForm()
    return render(request, 'suboverview.html', {'form': form})