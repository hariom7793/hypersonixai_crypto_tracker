from django.urls import path

from crypto_tracker.currency_prices.api.views import (
    currency_view, price_history_view
)

app_name = "currency_prices"
urlpatterns = [
    path("currencies/", view=currency_view, name="currency"),
]
