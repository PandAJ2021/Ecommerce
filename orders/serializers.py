from rest_framework import serializers
from .models import Address, Order
from cart.serializers import CartSerializer


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['province', 'city', 'street', 'code']


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    address = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['cart', 'address', 'created_at', 'status']
