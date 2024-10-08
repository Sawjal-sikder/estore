from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator
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


def productByBrand(request, slug):
    singleBrand = Brand.objects.get(slug=slug)
    all_product = Product.objects.filter(is_active=True, brand=singleBrand)
    paginator = Paginator(all_product, 10, orphans=1, allow_empty_first_page=True)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj}
    context.update(getShareContext())  # Merge shared context into the main context
    return render(request, 'product/product-list.html', context)


def productList(request):
    sort_by = request.GET.get('sort', 'Product sort by')  # Default to 'newest' if no parameter is provided

    if sort_by == 'newest':
        products = Product.objects.filter(is_active=True).order_by('created_date')[:9]
    elif sort_by == 'popular':
        products = Product.objects.filter(is_Popular=True)
    else:
        all_product = Product.objects.filter(is_active=True)
        paginator = Paginator(all_product, 10, orphans=1, allow_empty_first_page=True)
        page_number = request.GET.get("page")
        products = paginator.get_page(page_number)
    context = {'products': products, 'sort_by': sort_by}
    context.update(getShareContext())  # Merge shared context into the main context
    return render(request, 'product/product-list.html', context)


def categoryProduct(request, slug):
    singleCategory = Category.objects.get(slug=slug)
    all_product = Product.objects.filter(is_active=True, category=singleCategory)
    paginator = Paginator(all_product, 10, orphans=1, allow_empty_first_page=True)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj}
    context.update(getShareContext())  # Merge shared context into the main context
    return render(request, 'product/product-list.html', context)


def searchProduct(request):
    all_product = Product.objects.none()
    if request.method == "GET":
        product = request.GET.get('product', '')
        if product:
            all_product = Product.objects.filter(is_active=True, name__icontains=product)
    paginator = Paginator(all_product, 10, orphans=1, allow_empty_first_page=True)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj, 'product': product}
    context.update(getShareContext())  # Merge shared context into the main context
    return render(request, 'product/product-list.html', context)


def productDetails(request, slug):
    oneProduct = Product.objects.get(slug=slug)
    categoryOne = oneProduct.category
    relatedproduct = categoryOne.products.all()
    context = {
        "product": oneProduct,
        "relatedproduct": relatedproduct,
    }
    context.update(getShareContext())
    return render(request, 'product/product-detail.html', context)
