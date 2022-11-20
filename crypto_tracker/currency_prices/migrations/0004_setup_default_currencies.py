# Generated by Django 4.0.8 on 2022-11-20 16:35

from django.db import migrations, models

DEFAULT_CURRENCIES = [
    {'code': 'BTCUSDT', 'active': True},
    {'code': 'BNBUSDT', 'active': True},
    {'code': 'BNBETH', 'active': True},
    {'code': 'ETHUSDT', 'active': True},
    {'code': 'HSRBTC', 'active': True},
    {'code': 'GASBTC', 'active': False}
]

def setup_default_currencies(apps, schema_editor):
    Currency = apps.get_model("currency_prices", "Currency")
    Currency.objects.bulk_create([
        Currency(code=currency['code'], active=currency['active']) for currency in DEFAULT_CURRENCIES
    ])

def remove_default_currencies(apps, schema_editor):
    Currency = apps.get_model("currency_prices", "Currency")
    Currency.objects.filter(code__in=[currency['code'] for currency in DEFAULT_CURRENCIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('currency_prices', '0003_alter_pricehistory_currency'),
    ]

    operations = [
        migrations.RunPython(setup_default_currencies, remove_default_currencies)
    ]
