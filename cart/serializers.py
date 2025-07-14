from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    price = serializers.ReadOnlyField(source='get_price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity', 'added_at']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField(source='get_total_price')
    total_quantity = serializers.ReadOnlyField(source='get_total_quantity')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'is_active', 'created_at', 'updated_at', 'cart_items', 'total_price', 'total_quantity']
        read_only_fields = ['user']