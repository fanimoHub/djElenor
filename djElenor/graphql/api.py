import graphene
import graphql_jwt
from django.urls import reverse
from django.utils.functional import SimpleLazyObject
# from graphql import (
#     GraphQLCachedBackend,
#     GraphQLCoreBackend,
#     GraphQLScalarType,
#     GraphQLSchema,
#     execute,
#     parse,
#     validate,
# )
# from graphql.backend.base import GraphQLDocument
# from graphql.execution import ExecutionResult

# from ..core.utils.cache import CacheDict
# from ..graphql.notifications.schema import ExternalNotificationMutations
from ..account.schema import AccountMutations, AccountQueries
# from .app.schema import AppMutations, AppQueries
# from .attribute.schema import AttributeMutations, AttributeQueries
# from .channel.schema import ChannelMutations, ChannelQueries
# from .checkout.schema import CheckoutMutations, CheckoutQueries
# from .core.enums import unit_enums
# from .core.federation.schema import build_federated_schema
# from .core.schema import CoreMutations, CoreQueries
# from .csv.schema import CsvMutations, CsvQueries
# from .discount.schema import DiscountMutations, DiscountQueries
# from .giftcard.schema import GiftCardMutations, GiftCardQueries
# from .invoice.schema import InvoiceMutations
# from .menu.schema import MenuMutations, MenuQueries
# from .meta.schema import MetaMutations
# from .order.schema import OrderMutations, OrderQueries
# from .page.schema import PageMutations, PageQueries
# from .payment.schema import PaymentMutations, PaymentQueries
# from .plugins.schema import PluginsMutations, PluginsQueries
from ..product.schema import ProductQueries

# from .shipping.schema import ShippingMutations, ShippingQueries
# from .shop.schema import ShopMutations, ShopQueries
# from .tax.schema import TaxMutations, TaxQueries
# from .translations.schema import TranslationQueries
# from .warehouse.schema import (
#     StockMutations,
#     StockQueries,
#     WarehouseMutations,
#     WarehouseQueries,
# )
# from .webhook.schema import WebhookMutations, WebhookQueries
# from .webhook.subscription_types import WEBHOOK_TYPES_MAP, Subscription


API_PATH = SimpleLazyObject(lambda: reverse("api"))


class Query(
    AccountQueries,
    # AppQueries,
    # AttributeQueries,
    # ChannelQueries,
    # CheckoutQueries,
    # CoreQueries,
    # CsvQueries,
    # DiscountQueries,
    # PluginsQueries,
    # GiftCardQueries,
    # MenuQueries,
    # OrderQueries,
    # PageQueries,
    # PaymentQueries,
    ProductQueries,
    # ShippingQueries,
    # ShopQueries,
    # StockQueries,
    # TaxQueries,
    # TranslationQueries,
    # WarehouseQueries,
    # WebhookQueries,
):
    pass


class Mutation(
     AccountMutations,
#     # AppMutations,
#     # AttributeMutations,
#     # ChannelMutations,
#     # CheckoutMutations,
#     # CoreMutations,
#     # CsvMutations,
#     # DiscountMutations,
#     # ExternalNotificationMutations,
#     # PluginsMutations,
#     # GiftCardMutations,
#     # InvoiceMutations,
#     # MenuMutations,
#     # MetaMutations,
#     # OrderMutations,
#     # PageMutations,
#     # PaymentMutations,
#     # ProductMutations,
#     # ShippingMutations,
#     # ShopMutations,
#     # StockMutations,
#     # TaxMutations,
#     # WarehouseMutations,
#     # WebhookMutations,
 ):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
#     pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    # types=list(types) + [_Any, _Entity, _Service],
    # subscription=subscription,
    # directives=directives,
)
