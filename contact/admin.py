from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'address', 'phone', 'email']
    search_fields = ['company_name', 'address', 'phone', 'email']
    list_filter = ['company_name', 'address', 'phone', 'email']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    search_fields = ['name', 'address', 'phone']
    list_filter = ['name', 'address', 'phone']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','message']
    search_fields = ['name', 'email', 'subject','message']
    list_filter = ['name', 'email', 'subject','message']
