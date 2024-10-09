from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CartItem)
class cartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', ]
