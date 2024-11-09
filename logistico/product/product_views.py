from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from logistico.product.product_filters import ProductFilter
from .product import Product
from .product_serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter