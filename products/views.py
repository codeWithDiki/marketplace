from re import template
from django.views.generic import DetailView, RedirectView, ListView
from .models import *
from django.http import Http404
from django.conf import settings
import json

# View untuk menampilkan produk
class ProductDetailView(DetailView):
    model = Products
    slug_field = 'product_slugify'
    template_name = 'products/index.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
            
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
            
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
            
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            
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
            sort["comments"] = Rating.objects.filter(product=obj.id)[:10]

            obj.product_rating = sort


        return obj

# View untuk menampilkan category plus list view untuk produk dengan category yang diambil
class CategoryListView(ListView):
    template_name="products/category.html"
    model = Products
    paginate_by=12

    def setup(self, request, *args, **kwargs):
        if hasattr(self, 'get') and not hasattr(self, 'head'):
            self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs
        
        is_exists = Category.objects.filter(id=kwargs["pk"]).count() or None
        
        

        # check jika kategori tersedia
        if is_exists != None and is_exists > 0:
            # menambahkan context berupa kategori yang ingin ditampilkan
            self.extra_context = {
                "current_category" : Category.objects.get(id=kwargs["pk"]),
                "categories" : Category.objects.all()
            }

            # check database driver
            if settings.DATABASES['default']['ENGINE'] not in ['django.db.backends.sqlite3', 'django.db.backends.oracle']:
                # mengambil data dari model jika driver database bukan oracle atau sqlite 3
                self.queryset = self.model.objects.filter(product_category__contains=kwargs["pk"])
            else :
                # mengambil data dari model jika driver database merupakan oracle atau sqlite3
                queryset = self.model.objects.all()
                setter = []
                for products in queryset:
                    cat = products.product_category

                    if kwargs["pk"] in cat:
                        setter.append(products.id)

                self.queryset = self.model.objects.filter(id__in=setter)
            
        else :
            # menampilkan 404 jika kategori tidak ditemukan
            self.template_name="404.html"

    
        

# Redirect ke home root
class HomeRedirectView(RedirectView):
    pattern_name = "home_root"