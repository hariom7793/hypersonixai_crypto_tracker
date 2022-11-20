from rest_framework import viewsets

from currency_prices.serializers import CurrencySerializer, PriceHistorySerializer
from currency_prices.models import Currency, PriceHistory


class CurrencyViewSet(viewsets.ModelViewSet):
   queryset = Currency.objects.filter(active=True)
   serializer_class = CurrencySerializer


currency_view = CurrencyViewSet.as_view()


class PriceHistoryViewSet(viewsets.ModelViewSet):
   queryset = PriceHistory.objects.all()
   serializer_class = PriceHistorySerializer


price_history_view = PriceHistoryViewSet.as_view()
