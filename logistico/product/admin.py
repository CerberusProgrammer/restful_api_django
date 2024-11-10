from django.contrib import admin
from .product import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'state', 'creation_date', 'modification_date')
    search_fields = ('name', 'description')