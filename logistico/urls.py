from django.urls import path, include

urlpatterns = [
    path('', include('logistico.product.product_urls')),
    path('', include('logistico.subasta.subasta_urls')),
]