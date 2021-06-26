from rest_framework import viewsets
from products.models import Products
from .serializers import *
from django.views.generic import TemplateView

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class LandingPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        self.extra_context = {
            "webName" : "Marketplace"
        }
        return super().get_context_data(**kwargs)