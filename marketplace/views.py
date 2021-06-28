from rest_framework import viewsets
from products.models import Products
from .serializers import *
from django.views.generic import TemplateView, DetailView, detail
from products.models import *
from products.forms import *
from django.conf import settings



class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class LandingPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        product_in_category = {}

        for category in Category.objects.all():
            if settings.DATABASES['default']['ENGINE'] not in ['django.db.backends.sqlite3', 'django.db.backends.oracle']:
                products = Products.objects.filter(product_category__contains=category.id)[:8]
                for product in products:
                    product_item = {
                        "name"      : product.product_name,
                        "stock"     : product.product_stock,
                        "price"     : product.product_price,
                        "category"  : []
                    }

                    for pro_cat in product.product_category:
                        cat_in_pro = Category.objects.get(id = pro_cat)
                        product_item["category"].append(cat_in_pro.name)

                    
                    if category.name not in product_in_category:
                        product_in_category.update({category.name : [product_item]})
                    else :
                        if len(product_in_category[category.name]) < 8:
                            product_in_category[category.name].append(product_item)
            else :
                products = Products.objects.all()
                for product in products:
                    product_item = {
                        "pk"        : product.id,
                        "name"      : product.product_name,
                        "stock"     : product.product_stock,
                        "price"     : product.product_price,
                        "slug"      : product.product_slugify,
                        "category"  : []
                    }

                    for pro_cat in product.product_category:
                        cat_in_pro = Category.objects.get(id = pro_cat)
                        product_item["category"].append(cat_in_pro.name)

                    if category.id in product.product_category:
                        if category.name not in product_in_category:
                            product_in_category.update({category.name : [product_item]})
                        else :
                            if len(product_in_category[category.name]) < 8:
                                product_in_category[category.name].append(product_item)
        
        

        self.extra_context = {
            "webName" : "Marketplace",
            "category" : Category.objects.all(),
            "product_in_category" : product_in_category.items()
        }
        return super().get_context_data(**kwargs)

class ProductDetailView(DetailView):
    model = Products
    slug_field = 'product_slugify'

    def get_object(self, queryset=None):
        
        if queryset != None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if pk != None :
            queryset = queryset.filter(pk=pk)
        
        if slug != None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        
        if pk == None and slug == None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        
        try:
        # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
