from django.contrib import admin
from .subasta import Subasta

@admin.register(Subasta)
class SubastaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'state', 'creation_date', 'modification_date')
    search_fields = ('name', 'description')