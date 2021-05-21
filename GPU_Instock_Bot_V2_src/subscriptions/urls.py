from django.urls import path
from subscriptions.views import subscriptionview

urlpatterns = [
    path('', subscriptionview, name='subscriptionsview'),
]