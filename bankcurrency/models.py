from django.db import models
from django.utils import timezone


class CurrencyAuthUser(models.Model):
    """для авторизованных пользователей"""
    ALPHABANK = 'alfabank'
    BELAGROPROMBANK = 'belagro'
    BELARUSBANK = 'belbank'

    BANKS = [
        (ALPHABANK, 'alfabank'),
        (BELAGROPROMBANK, 'belagro'),
        (BELARUSBANK, 'belbank'),
    ]
    company = models.CharField(max_length=255, choices=BANKS, blank=False)
    date = models.DateTimeField(verbose_name='Дата Курса Валют', default=timezone.now)
    eur_buy = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Покупка EUR')
    eur_sell = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Продажа EUR')
    usd_buy = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Покупка USD')
    usd_sell = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Продажа USD')
    rur_buy = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Покупка RUR')
    rur_sell = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Продажа RUR')

    class Meta:
        verbose_name = 'currency'
        db_table = 'currency_auth_user'

    def __str__(self):
        return self.company


class CurrencyUnAuthUser(models.Model):
    """для неавторизованных пользователей"""
    ALPHABANK = 'alfabank'
    BELAGROPROMBANK = 'belagro'
    BELARUSBANK = 'belbank'

    BANKS = [
        (ALPHABANK, 'alfabank'),
        (BELAGROPROMBANK, 'belagro'),
        (BELARUSBANK, 'belbank'),
    ]
    company = models.CharField(max_length=255, choices=BANKS, blank=False)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Продажа USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Продажа RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Продажа EUR")

    class Meta:
        verbose_name = 'currency'
        db_table = 'currency_un_auth_user'

    def __str__(self):
        return self.company
