from django.contrib import admin
from .models import Category, Product
from django.contrib.admin import ModelAdmin


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    model = Category
    list_display = ['id', 'name', 'description', 'parent', 'is_active']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    model = Product
    list_display = ['id', 'name', 'description', 'category', 'price', 'is_active']