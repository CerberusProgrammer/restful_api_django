from django.urls import path, include
from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]