from django.contrib import admin
from .product import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'state', 'creation_date', 'modification_date')
    search_fields = ('name', 'description')
    list_filter = ('state', 'creation_date', 'modification_date')
    date_hierarchy = 'creation_date'
    ordering = ('-creation_date',)
    readonly_fields = ('creation_date', 'modification_date')