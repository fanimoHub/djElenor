from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category,
        related_name='subCategories',
        on_delete=models.CASCADE
    )


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    subCategory = models.ForeignKey(
        SubCategory,
        related_name='products',
        on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.PositiveIntegerField()
    amount_in_stock = models.PositiveIntegerField()


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='productImages/')


class Rating(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    stars = models.PositiveIntegerField()
    note = models.TextField()
    rating_from = models.ForeignKey(
        User,
        related_name='ratings_given',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='comments',
        on_delete=models.CASCADE
    )
    comment_from = models.ForeignKey(
        User,
        related_name='comments_given',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
