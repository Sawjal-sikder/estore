from django.urls import path
from .views import *

urlpatterns = [
    path('', productList, name="productlist"),
    path('details/', productDetails, name="productdetails"),
]
