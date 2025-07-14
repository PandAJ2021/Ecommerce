from rest_framework import viewsets
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cart.objects.all()
        return Cart.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user, cart__is_active=True)
    
    def perform_create(self, serializer):
        try:
            cart = get_object_or_404(Cart, user=self.request.user, is_active=True)
        except:
            raise ValidationError('No active cart found for user')
        
        serializer.save(cart=cart)

