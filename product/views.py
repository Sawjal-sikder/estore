from django.shortcuts import render


# Create your views here.

def productList(request):
    return render(request, 'product/product-list.html')


def productDetails(request):
    return render(request, 'product/product-detail.html')
