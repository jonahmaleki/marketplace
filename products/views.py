from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product

class ProductListView(ListView):
    # model = Product
    # or
    # queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
