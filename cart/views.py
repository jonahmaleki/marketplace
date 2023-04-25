from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _


from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        inplace = cleaned_data['inplace']
        cart.add(product, quantity, current_replace_quantity=inplace)

    return redirect('product_list')


def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('cart:cart_detail')


def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('successfully cart clear'))
    else:
        messages.warning((request, _('your cart is empty , dont need to clear')))

    return render(request, 'cart/cart_detail.html')