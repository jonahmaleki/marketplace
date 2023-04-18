from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(ListView):
    # model = Product
    # or
    # queryset = Product.objects.filter(active=True)
    paginate_by = 4
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

