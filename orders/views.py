from .serializers import OrderSerializer
from rest_framework import viewsets , mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import AddressSerializer, OrderSerializer
from .models import Address, Order
from cart.models import Cart
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 


class OrderViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        user = self.request.user
        address_id = self.request.query_params.get('address_id')
        if not address_id:
            raise ValidationError("address_id query parameter is required")

        address = get_object_or_404(Address, user=user, id=address_id)
        cart = get_object_or_404(Cart, user=user, is_active=True)
        cart.is_active = False
        cart.save()

        serializer.save(user=user, cart=cart, address=address)

    def perform_destroy(self, instance):
        if instance.status in ['cancelled', 'delivered']:
            raise ValidationError('This order cannot be cancelled')
        instance.status = 'cancelled'
        instance.save()