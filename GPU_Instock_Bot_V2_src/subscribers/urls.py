from django.urls import path
from subscribers.views import subscriptionview

urlpatterns = [
    path('', subscriptionview, name='subscriptionview'),
]