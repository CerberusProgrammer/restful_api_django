from rest_framework import serializers
from .subasta import Subasta

class SubastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subasta
        fields = '__all__'