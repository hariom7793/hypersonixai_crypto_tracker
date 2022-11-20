from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from crypto_tracker.users.api.views import UserViewSet
from crypto_tracker.currency_prices.api.views import CurrencyViewSet, PriceHistoryViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("currencies", CurrencyViewSet)
router.register("price_history", PriceHistoryViewSet)

app_name = "api"
urlpatterns = router.urls
