from .models import User
import graphene
#
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User


# ...code
class AccountQueries(graphene.ObjectType):
    users = graphene.List(UserType)
    viewer = graphene.Field(UserType)

    def resolve_viewer(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided !!!!!")
        return user

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
