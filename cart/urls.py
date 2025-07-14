from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.CartViewSet, basename='cart')
router.register(r'cart-items', views.CartItemViewSet, basename='cartitem')

app_name = 'cart'
urlpatterns = [] 
urlpatterns+= router.urls