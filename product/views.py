from django.shortcuts import render
from .models import *


# Create your views here.

def productList(request):

    all_product = Product.objects.filter(is_active=True)
    short_product = Product.objects.filter(is_active=True).order_by('-created_date')[:3]
    categories = Category.objects.filter(is_active=True)
    brands = Brand.objects.filter(is_active=True)

    context = {
        'products': all_product,
        'categories': categories,
        'brands': brands,
        'short_product': short_product,
    }

    return render(request, 'product/product-list.html', context)


def productDetails(request):
    return render(request, 'product/product-detail.html')
