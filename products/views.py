from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm

class ProductListView(generic.ListView):
    # model = Product
    # or
    # queryset = Product.objects.filter(active=True)
    paginate_by = 4
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_product_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    # success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        messages.success(request=self.request, message='your comment successfully add.')
        return super().form_valid(form)

