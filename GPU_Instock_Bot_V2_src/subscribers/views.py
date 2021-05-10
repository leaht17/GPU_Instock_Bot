from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import SubscriptionForm
from django.http import HttpResponseRedirect


# Create your views here.
from .models import Subscriber


def subscriptionview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # counter = 0
            # gpu_list = form.cleaned_data['gpus']
            # email = form.cleaned_data['email']
            # phone = form.cleaned_data['phone']
            # print(email)
            # print(phone)
            # print(gpu_list)
            # for gpu in gpu_list:
            #     gpu.save()
            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriptionForm()
    return render(request, 'suboverview.html', {'form': form})
