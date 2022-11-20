from django.contrib import admin
from currency_prices.models import Currency, PriceHistory

admin.site.register(Currency)
admin.site.register(PriceHistory)
