from rest_framework import viewsets
from products.models import Products
from .serializers import *
from django.views.generic import TemplateView
from products.models import *

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class LandingPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        product_in_category = {}

        for category in Category.objects.all():
            products = Products.objects.all()[:8]
            for product in products:
                product_item = {
                    "name" : product.product_name,
                    "stock" : product.product_stock,
                    "price" : product.product_price,
                }
                if category.id in product.product_category:
                    if category.name not in product_in_category:
                        product_in_category.update({category.name : [product_item]})
                    else :
                        product_in_category[category.name].append(product_item)
        
        

        self.extra_context = {
            "webName" : "Marketplace",
            "category" : Category.objects.all(),
            "product_in_category" : product_in_category.items()
        }
        return super().get_context_data(**kwargs)