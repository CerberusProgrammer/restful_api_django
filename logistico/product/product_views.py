from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .product import Product
from .product_filters import ProductFilter
from .product_serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = ProductPagination
    ordering_fields = ['name', 'price', 'stock', 'state', 'creation_date', 'modification_date']
    ordering = ['name']