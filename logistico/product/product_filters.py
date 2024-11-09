import django_filters
from .product import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    price = django_filters.NumberFilter(field_name='price')
    stock = django_filters.NumberFilter(field_name='stock')
    state = django_filters.BooleanFilter(field_name='state')
    creation_date = django_filters.DateTimeFilter(field_name='creation_date')
    modification_date = django_filters.DateTimeFilter(field_name='modification_date')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'state', 'creation_date', 'modification_date']