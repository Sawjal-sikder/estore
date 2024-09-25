from django.urls import path
from .views import *

urlpatterns = [
    path('', productList, name="productlist"),
    path('search/', searchProduct, name="search"),
    path('details/', productDetails, name="productdetails"),
    path('details/categoryProduct/<slug:slug>', categoryProduct, name="categoryProduct"),
    path('details/brand/<slug:slug>', productByBrand, name="productByBrand"),
]
