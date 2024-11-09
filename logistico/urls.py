from django.urls import path, include

urlpatterns = [
    path('', include('logistico.product.product_urls')),
]