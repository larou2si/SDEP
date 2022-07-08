from django.urls import path
from .views import *

app_name = 'dsserver'
urlpatterns = [
    path('', dashboard, name='dashboard'),

    ]