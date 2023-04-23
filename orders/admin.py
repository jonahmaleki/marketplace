from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Order, OrderItem


class OrderItemInline(TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 0


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['user', 'first_name', 'phone_number', 'is_paid']

    inlines = [
        OrderItemInline
    ]


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']