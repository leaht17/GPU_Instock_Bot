from django.shortcuts import render
from .models import SubscriberCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
def suboverview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriberCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriberCreationForm()
    return render(request, 'suboverview.html', {'form': form})
