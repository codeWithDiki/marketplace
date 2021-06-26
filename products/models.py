from django.db import models
from django.db.models.enums import Choices
from django.utils.text import slugify
import re

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=50, blank=False)
    product_description = models.TextField(default="My Product", blank=False)
    product_price = models.FloatField(blank=False)
    product_category = models.JSONField(blank=False)
    product_created = models.DateTimeField(auto_now_add=True)
    product_updated = models.DateTimeField(auto_now=True)
    product_owner = models.CharField(max_length=25, editable=False, blank=False)
    product_stock = models.IntegerField(blank=False)
    product_rating = models.FloatField(editable=False)
    product_slugify = models.SlugField(editable=False)

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
        rating.append(self.rate)
        average = sum(rating) / len(rating)
        product.update({"product_rating" : float(average)})
        product.save()
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=False)

class Discount(models.Model):
    product = models.IntegerField(blank = False, editable=False)
    name = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=False)
    discount = models.FloatField(blank=False)




