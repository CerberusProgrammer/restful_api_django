from rest_framework import serializers

from logistico.product.product_serializers import ProductSerializer
from .subasta import Subasta

class SubastaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subasta
        fields = '__all__'

class SubastaDetailedSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Subasta
        fields = '__all__'