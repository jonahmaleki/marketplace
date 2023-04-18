from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['body', 'author', 'is_active', 'stars', 'recommend']
    extra = 0

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['title', 'price', 'active']

    inlines = [
        CommentInline
    ]
@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['body', 'author', 'is_active', 'stars', 'recommend', 'product']

