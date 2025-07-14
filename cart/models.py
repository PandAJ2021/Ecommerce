from django.db import models
from accounts.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s cart"
    
    @property
    def get_total_price(self):
        return sum(item.get_price for item in self.cart_items.all())
    
    @property
    def get_total_quantity(self):
        return sum(item.quantity for item in self.cart_items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'cart'], name='unique_cart_product')
        ]

    def __str__(self):
        return f'{self.quantity} X {self.product.name} in cart #{self.cart.id}'
    
    @property
    def get_price(self):
        return self.product.price * self.quantity