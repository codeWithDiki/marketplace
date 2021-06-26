from django.db import models
from django.utils.text import slugify
import re

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(default="My Product")
    product_price = models.FloatField()
    product_category = models.JSONField()
    product_created = models.DateTimeField(auto_now_add=True)
    product_updated = models.DateTimeField(auto_now=True)
    product_owner = models.CharField(max_length=25)
    product_stock = models.IntegerField()
    product_rating = models.FloatField()
    product_slugify = models.SlugField()

    def __str__(self):
        return "{}".format(self.product_name)

    def save(self, *args, **kwargs):
        self.product_slugify = slugify(self.product_name)
        super().save(*args, **kwargs)
