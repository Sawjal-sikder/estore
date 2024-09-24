from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=55, default='fa fa-circle', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='category_thumbnails/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='categories_created')
    created_date = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='categories_updated')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='brand_thumbnails/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='brands_created')
    created_date = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='brands_updated')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
    ]

    # Define choices for size
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    thumbnail = models.ImageField(upload_to='product_thumbnails/', blank=True, null=True)
    image1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    new_price = models.PositiveIntegerField(default=0, blank=True, null=True)
    old_price = models.PositiveIntegerField(default=0, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, blank=True, null=True)  # Add size choices
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True, null=True)  # Add color choices
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='products_created')
    created_date = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='products_updated')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
