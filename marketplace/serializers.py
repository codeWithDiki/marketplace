from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from products.models import Products

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['url', 'product_name', 'product_description', 'product_stock', 'product_images']