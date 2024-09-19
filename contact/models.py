from django.db import models


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/')
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_link = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class Store(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='storedetails')
    name = models.CharField(max_length=55)
    address = models.TextField()
    phone = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
