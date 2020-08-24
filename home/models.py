from django.db import models


# Create your models here.


class Home(models.Model):
    # About us
    about_us = models.TextField(blank=False)
    درباره_ما = models.TextField(blank=False, default='درباره ما')
    # Contact Us
    phone = models.CharField(max_length=50)
    موبایل = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=50)
    تلفن_شرکت = models.CharField(max_length=50)
    address = models.TextField()
    آدرس = models.TextField()
    email = models.EmailField()
    ایمیل = models.EmailField()
    site_develoepr = models.BooleanField(default=True)
