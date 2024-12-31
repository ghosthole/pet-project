from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inbox, name='inbox'),
    path('today/', today, name='today'),
]
