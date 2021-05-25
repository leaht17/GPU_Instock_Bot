from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from .models import Subscription
from django.db.models import Q
from django.contrib import messages

# Create your views here.
from subscribers.models import Subscriber


def subscriptionview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriptionForm(request.POST)

        # establish initial values
        email = ''
        phone = ''
        gpu_list = None
        subscriber = None

        # if form is valid then populate values
        if form.is_valid():
            if form.cleaned_data.__contains__('email'):
                email = form.cleaned_data['email']
            if form.cleaned_data.__contains__('phone'):
                phone = form.cleaned_data['phone']
            if form.cleaned_data.__contains__('gpus'):
                gpu_list = form.cleaned_data['gpus']

        # otherwise return
        else:
            return render(request, 'suboverview.html', {'form': form})

        # if email and phone are both empty then scold user
        if email == '' and phone == '':
            messages.error(request, 'At least one of email or phone is required for un/re/subscription.')
            return render(request, 'suboverview.html', {'form': form})

        # otherwise query the subscriber with the provided info
        else:
            subscriber = Subscriber.objects.filter(Q(email=email) | Q(phone=phone))

        # retrieve number of subscribers with this info, should be <= 2
        subcount = subscriber.count()

        # if unsubscription request is received then process it
        if 'unsubscribe' in request.POST:

            # if user is not already subscribed then scold user
            if subcount == 0:
                messages.error(request, 'Unsubscription was unsuccessful! No subscriber information associated with the'
                                        ' provided credential(s) was found in our database.')
                print('no subscriber found')

            # otherwise remove the user's subscriptions and data
            else:
                subscriber.delete()
                messages.success(request, 'You are now unsubscribed from our service! Your associated data will now be '
                                          'removed from our database')
                print("subscriber deleted")

        # if re/subscription request is received then process it
        elif 'subscribe' in request.POST:

            # if gpu list is empty then scold user
            if gpu_list.count() == 0:
                messages.error(request, 'Re/Subscription unsuccessful! You have not selected any GPUs to re/subscribe '
                                        'to.')
                print('no gpus selected')

            # if subscriber does not exist then subscribe them
            elif subcount == 0:
                # save the form
                form.save()
                messages.success(request, 'You are now subscribed! We will notify you when one of your selected GPUs '
                                          'is in stock.')
                print("subscriber created. subscriptions added")

            # if subscriber already exists then re-subscribe them
            elif subcount == 1:

                # if subscriber added a phone or email on resubscribe but previously did not have one then
                if subscriber[0].email == email and subscriber[0].phone != phone and phone != '':
                    subscriber.update(phone=phone)
                    messages.success(request, 'Your phone number was updated upon re-subscription')
                if subscriber[0].phone == phone and subscriber[0].email != email and email != '':
                    subscriber.update(email=email)
                    messages.success(request, 'Your email was updated upon re-subscription.')

                # delete existing subscriptions
                Subscription.objects.filter(sub_subscriber=subscriber[0]).delete()

                # add new subscriptions
                for gpu in gpu_list:
                    Subscription.objects.create(sub_subscriber=subscriber[0], sub_gpu=gpu)
                messages.success(request, 'You are now re-subscribed! We will notify you when one of your re-selected '
                                          'GPUs is in stock.')

                print("subscribers subscriptions updated")

            # if subscriber already exists then re-subscribe them
            elif subcount == 2:

                # delete existing subscriptions
                for sub in subscriber:
                    Subscription.objects.filter(sub_subscriber=sub).delete()

                # merge subscriber info
                subscriber[0].delete()
                subscriber[1].delete()

                # add new subscriptions
                new_subscriber = Subscriber.objects.create(email=email, phone=phone)
                for gpu in gpu_list:
                    Subscription.objects.create(sub_subscriber=new_subscriber, sub_gpu=gpu)
                messages.success(request, 'You are now re-subscribed! We will notify you when one of your re-selected '
                                          'GPUs is in stock.')

                print("subscribers subscriptions updated")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriptionForm()
    return render(request, 'suboverview.html', {'form': form})