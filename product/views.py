from django.shortcuts import render
from django.db.models import Count
from .models import *


# Create your views here.
def getShareContext():
    short_product = Product.objects.filter(is_active=True).order_by('-created_date')[:3]
    categories = Category.objects.filter(is_active=True)
    brands = Brand.objects.filter(is_active=True).annotate(product_count=Count('products'))
    return {
        'categories': categories,
        'brands': brands,
        'short_product': short_product,
    }


def productList(request):
    all_product = Product.objects.filter(is_active=True)
    context = {'products': all_product}
    context.update(getShareContext())  # Merge shared context into the main context
    return render(request, 'product/product-list.html', context)


def categoryProduct(request, slug):
    singleCategory = Category.objects.get(slug=slug)
    all_product = Product.objects.filter(is_active=True, category=singleCategory)
    context = {
        'products': all_product,
    }
    context.update(getShareContext())
    return render(request, 'product/product-list.html', context)


def productByBrand(request, slug):
    singleBrand = Brand.objects.get(slug=slug)
    all_product = Product.objects.filter(is_active=True, brand=singleBrand)
    context = {
        'products': all_product,
    }
    context.update(getShareContext())
    return render(request, 'product/product-list.html', context)


def searchProduct(request):
    all_product = Product.objects.none()
    if request.method == "GET":
        product = request.GET.get('product', '')
        if product:
            all_product = Product.objects.filter(is_active=True, name__icontains=product)
    context = {'products': all_product, }
    context.update(getShareContext())
    return render(request, 'product/product-list.html', context)


def productDetails(request):
    return render(request, 'product/product-detail.html')
