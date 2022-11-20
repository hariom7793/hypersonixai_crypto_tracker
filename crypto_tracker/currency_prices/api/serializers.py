from rest_framework import serializers

from currency_prices.models import Currency, PriceHistory


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('code', 'active')


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ('date', 'currency', 'price')
