from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_by', 'updated_by']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-id', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # This is a new object
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_by', 'updated_by']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-id', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # This is a new object
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'sku', 'size', 'color', 'slug', 'is_active', 'created_by',
                    'updated_by']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-id', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # This is a new object
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
