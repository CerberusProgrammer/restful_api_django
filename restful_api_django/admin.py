from django.contrib import admin

from logistico.product.product import Product
from logistico.subasta.subasta import Subasta

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'state', 'creation_date', 'modification_date')
    list_filter = ('state', 'creation_date', 'modification_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'creation_date'
    ordering = ('name', 'price')
    fields = ('name', 'description', 'price', 'stock', 'state')
    readonly_fields = ('creation_date', 'modification_date')

admin.site.register(Product, ProductAdmin)

class SubastaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'state', 'creation_date', 'modification_date')
    list_filter = ('state', 'creation_date', 'modification_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'creation_date'
    ordering = ('name', 'price')
    fields = ('name', 'description', 'price', 'stock', 'state')
    readonly_fields = ('creation_date', 'modification_date')

admin.site.register(Subasta, SubastaAdmin)