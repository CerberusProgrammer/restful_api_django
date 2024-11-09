# views
from django.shortcuts import render
from rest_framework import viewsets
from .product import Product
from .product_serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer