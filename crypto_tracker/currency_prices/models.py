from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.code


class PriceHistory(models.Model):
    date = models.DateTimeField()
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=12, decimal_places=2)
