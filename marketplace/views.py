from rest_framework import viewsets
from products.models import Products
from .serializers import *
from django.views.generic import TemplateView, DetailView, detail
from products.models import *
from products.forms import *
from django.conf import settings
from django.http import HttpResponse, Http404



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
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        
        if obj.product_rating is not None:
            temp = str(obj.product_rating).split(".")
            sort = {}

            sort["range"] = range(0, 5)
            sort["index"] = int(temp[0])
            sort["half"] = int(temp[1])
            sort["by"] = len(Rating.objects.filter(product=obj.id))
            sort["full_rate"] = "{}.{}".format(str(temp[0]), str(temp[1])[:2])
            sort["comments"] = Rating.objects.filter(product=obj.id)

            obj.product_rating = sort


        return obj
