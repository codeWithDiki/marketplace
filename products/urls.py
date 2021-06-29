from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:pk>/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
    path('<int:pk>', ProductDetailView.as_view(), name="product_detail")
]