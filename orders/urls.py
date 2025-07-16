from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'address', views.AddressViewSet, basename='address')
router.register(r'', views.OrderViewSet, basename='order')

app_name = 'orders'
urlpatterns = []
urlpatterns += router.urls