from django.urls import path, include
from . import views
from rest_framework import routers

admin_router = routers.SimpleRouter()
admin_router.register(r'products', views.ProductAdminViewSet)

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

    #Admin API
    path('admin/', include(admin_router.urls)),
]