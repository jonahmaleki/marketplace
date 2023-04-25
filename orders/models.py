from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email = models.CharField(max_length=150, blank=True, verbose_name=_('Email'))
    address = models.CharField(max_length=700, verbose_name=_('Address'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Phone Number'))
    order_note = models.CharField(max_length=300, blank=True, verbose_name=_('Order Note'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Modified'))

    def __str__(self):
        return f'{self.id}: {self.user}'

    def get_total_price(self):
        return sum(item.price * item.quntity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id} : {self.product} x {self.quantity} (price:{self.price})'