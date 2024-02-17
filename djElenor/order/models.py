from django.db import models
from ..product.models import Product
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('created', 'Created'),
    ('processing', 'Processing'),
    ('cancelled', 'Cancelled'),
    ('delivered', 'Delivered'),
]


class Order(models.Model):
    product = models.ForeignKey(Product,
                                related_name='orders',
                                on_delete=models.CASCADE)
    order_from = models.ForeignKey(User,
                                   related_name='orders_given',
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              default="created",
                              choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
