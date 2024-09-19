from django.urls import path
from .views import *

urlpatterns = [
    path('', profileUpdate.as_view(), name='profile_update'),

]
