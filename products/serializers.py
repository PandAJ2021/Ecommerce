from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductAdminSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductPublicSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'is_available', 'image']

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'description', 'price', 'image']