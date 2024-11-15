from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .subasta import Subasta
from .subasta_filters import SubastaFilter
from .subasta_serializers import SubastaSimpleSerializer, SubastaDetailedSerializer

class SubastaPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'

class SubastaViewSet(viewsets.ModelViewSet):
    queryset = Subasta.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SubastaFilter
    pagination_class = SubastaPagination
    ordering_fields = ['name', 'description', 'price', 'stock', 'state', 'creation_date', 'modification_date', 'product_id']
    ordering = ['name']

    def get_serializer_class(self):
        projection = self.request.query_params.get('projection', 'simple')
        if projection == 'detailed':
            return SubastaDetailedSerializer
        return SubastaSimpleSerializer