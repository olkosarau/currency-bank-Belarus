from django.db import models
from decimal import Decimal


class AlfaBank(models.Model):
    title = models.CharField(max_length=150, verbose_name='Валюта')
    usd = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="EUR")
    date = models.DateTimeField(auto_now=True)
    done = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        pass


