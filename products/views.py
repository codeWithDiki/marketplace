from django.views.generic import DetailView
from .models import *
from django.http import Http404

# Create your views here.
class ProductDetailView(DetailView):
    model = Products
    slug_field = 'product_slugify'
    template_name = 'products/index.html'

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
            sort["comments"] = Rating.objects.filter(product=obj.id)[:10]

            obj.product_rating = sort


        return obj

class CategoryDetailView(DetailView):
    model = Category