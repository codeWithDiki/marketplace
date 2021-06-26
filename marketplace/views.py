from rest_framework import viewsets
from products.models import Products
from .serializers import *

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer