from django.urls import path, include

urlpatterns = [
    path('products/', include('logistico.product.product_urls')),
    path('subastas/', include('logistico.subasta.subasta_urls')),
    path('viajes/', include('logistico.viaje.viaje_urls')),
]