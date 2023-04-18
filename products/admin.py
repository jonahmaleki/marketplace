from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['title', 'price', 'active']

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['body', 'author', 'is_active', 'stars', 'recommend', 'product']