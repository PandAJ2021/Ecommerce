from django.db import models
from accounts.models import User
from cart.models import Cart


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.province} | {self.city} | street:{self.street} | code:{self.code}'
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending','pending'),
        ('paid','paid'),
        ('processing','processing'),
        ('shipped','shipped'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')],
         default= 'pending')
    
    def __str__(self):
        return f"Order #{self.id} by {self.user} - {self.status}"