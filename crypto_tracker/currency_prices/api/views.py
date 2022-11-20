from rest_framework import viewsets

from currency_prices.models import Currency, PriceHistory
from .serializers import CurrencySerializer, PriceHistorySerializer
from rest_framework import viewsets


class CurrencyViewSet(viewsets.ModelViewSet):
   queryset = Currency.objects.all()
   serializer_class = CurrencySerializer

   def get_queryset(self):
      queryset = self.queryset
      active = self.request.query_params.get('active')
      code = self.request.query_params.get('code')
      if active is not None:
         queryset = queryset.filter(active=active)
      if code is not None:
         queryset = queryset.filter(code=code)
      return queryset


class PriceHistoryViewSet(viewsets.ModelViewSet):
   queryset = PriceHistory.objects.all()
   serializer_class = PriceHistorySerializer

   def get_queryset(self):
      queryset = self.queryset
      currency_code = self.request.query_params.get('currency_code')
      date = self.request.query_params.get('date')
      if currency_code is not None:
         queryset = queryset.filter(currency__code=currency_code)
      if date is not None:
         queryset = queryset.filter(date=date)
      return queryset
