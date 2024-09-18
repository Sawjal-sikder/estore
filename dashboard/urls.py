from django.urls import path
from .views import *

urlpatterns = [
    path('', my_account, name="my_account")
]