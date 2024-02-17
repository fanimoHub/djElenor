import graphene
from graphene_django import DjangoObjectType
from .models import (
    Category,
    SubCategory,
    Product,
    ProductImage,
    Rating,
    Comment,
)


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductQueries(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()
