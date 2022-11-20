import requests, json
from datetime import datetime
from .models import Currency, PriceHistory


def fetch_data(url, params=None):
    response = requests.get(url, params=params)
    return response.json()


def fetch_price_and_store():
    print('*'*10, 'Fetching data and storing', '*'*10)
    active_currencies = Currency.objects.filter(active=True).values_list('code', flat=True)
    params = {
        'symbols': json.dumps(list(active_currencies)).replace(' ', '')
    }
    response = fetch_data('https://api.binance.com/api/v3/ticker/price', params=params)
    for prices in response:
        PriceHistory.objects.create(
            date = datetime.utcnow(),
            currency=Currency.objects.get(code=prices['symbol']),
            price=prices['price']
        )
    print('*'*10, 'Done fetching data and storing', '*'*10)
