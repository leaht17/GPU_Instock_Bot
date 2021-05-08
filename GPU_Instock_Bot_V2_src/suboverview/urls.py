from django.urls import path
from suboverview import views

urlpatterns = [
    path('', views.suboverview, name='suboverview'),
]
