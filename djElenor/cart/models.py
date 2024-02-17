from django.db import models
from ..product.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    account = models.OneToOneField(
        User,
        related_name='cart',
        on_delete=models.CASCADE
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(Product, related_name='product')
    amount = models.PositiveIntegerField(default=1)
