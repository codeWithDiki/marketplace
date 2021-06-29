from django.db import models

# Create your models here.

class Invoice(models.Model):
    product                 = models.IntegerField()
    product_pieces          = models.IntegerField()
    buyers                  = models.IntegerField()
    payment_method          = models.CharField(max_length=50)
    invoice_request         = models.TextField()
    invoice_create_date     = models.DateTimeField(auto_now_add=True)
    invoice_status          = models.CharField(max_length=25)
    invoice_price           = models.FloatField()
    invoice_status_time     = models.JSONField()
    invoice_courier         = models.IntegerField()
    invoice_receipt_number  = models.CharField(max_length=30)

class Courier(models.Model):
    name        = models.CharField(max_length = 25)
    description = models.TextField()
    api         = models.JSONField()

class PaymentMethod(models.Model):
    name        = models.CharField(max_length=25)
    description = models.TextField()
    api         = models.JSONField()
