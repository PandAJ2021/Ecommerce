from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductAdminSerializer, ProductDetailSerializer, ProductPublicSerializer
from rest_framework.permissions import IsAdminUser

class ProductListView(ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductPublicSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'

class ProductAdminViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer
    permission_classes = [IsAdminUser]