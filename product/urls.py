from django.urls import path
from .views import *

urlpatterns = [
    path('', productList, name="productlist"),
    path('search/', searchProduct, name="search"),
    path('category/<slug:slug>', categoryProduct, name="categoryProduct"),
    path('brand/<slug:slug>', productByBrand, name="productByBrand"),
    path('details/<slug:slug>', productDetails, name="productdetails"),
]
