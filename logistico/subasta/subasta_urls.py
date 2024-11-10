from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .subasta_views import SubastaViewSet

router = DefaultRouter()
router.register(r'subastas', SubastaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]