from django.db import models
from django.db.models.enums import Choices
from django.utils.text import slugify
import re

# Create your models here.

class Products(models.Model):
    product_name        = models.CharField(max_length=50, blank=False)
    product_description = models.TextField(default="My Product", blank=False)
    product_price       = models.FloatField(blank=False)
    product_category    = models.JSONField(blank=False)
    product_created     = models.DateTimeField(auto_now_add=True)
    product_updated     = models.DateTimeField(auto_now=True)
    product_owner       = models.CharField(max_length=25, editable=False, blank=False)
    product_stock       = models.IntegerField(blank=False)
    product_rating      = models.FloatField(editable=False, blank=True, null=True)
    product_media       = models.JSONField(blank=True, null=True)
    product_slugify     = models.SlugField(editable=False)
    product_condition   = models.CharField(blank=True, max_length=50)
    product_type        = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return "{}".format(self.product_name)

    def save(self, *args, **kwargs):
        self.product_slugify = slugify(self.product_name)
        return super().save(*args, **kwargs)


# CHOICES = ()

# for product in Products.objects.all():
#     CHOICES = CHOICES + (product["id"], product["product_name"])

class Rating(models.Model):
    product = models.IntegerField(blank=False)
    comments = models.TextField(default="Good Item!")
    rate = models.FloatField(blank=False)
    rater = models.IntegerField(blank=False)

    def __str__(self):
        return "Product ID :{}".format(self.product)

    def save(self, *args, **kwargs):
        product = Products.objects.get(id=self.product)
        rating = Rating.objects.filter(product=self.product).values("rate")
        
        rate_list = []

        for rate in rating:
            rate_list.append(rate["rate"])


        rate_list.append(self.rate)

        if len(rate_list) is not 0:
            average = sum(rate_list) / len(rate_list)
        else:
            average = self.rate
        
        product.product_rating = average
        product.save()
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(args, kwargs)

class Discount(models.Model):
    product = models.IntegerField(blank = False, editable=False)
    name = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=False)
    discount = models.FloatField(blank=False)


    




