# from django.contrib.auth import get_user_model
from .models import User
import graphene
# from graphene import relay, ObjectType
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User


# ...code
class AccountQueries(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class AccountMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
