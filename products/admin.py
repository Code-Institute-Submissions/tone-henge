from django.contrib import admin
from products.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
