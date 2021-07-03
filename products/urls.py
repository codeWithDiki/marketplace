from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/<int:pk>/<slug:slug>', CategoryListView.as_view(), name="category_detail_with_products"),
    path('category/<int:pk>', CategoryListView.as_view(), name="category_detail_with_products"),
    path('<int:pk>/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
    path('<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('category/', HomeRedirectView.as_view()),
    path('', HomeRedirectView.as_view())
]