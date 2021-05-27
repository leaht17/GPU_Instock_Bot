from django.urls import path
from subscribers.views import subscriptionview

# Set URL path for subscribers view
urlpatterns = [
    path('', subscriptionview, name='subscriptionview'),
]
