from django.db import models
from django.utils import timezone


class Auth(models.Model):
    """для авторизованных пользователей"""

    ALPHABANK = 'АльфаБанк'
    BELAGROPROMBANK = 'БелАгроПромБанк'
    BELARUSBANK = 'БеларусБанк'

    BANKS = [
        (ALPHABANK, 'Альфабанк'),
        (BELAGROPROMBANK, 'Белагропром'),
        (BELARUSBANK, 'Беларусбанк'),
    ]
    company = models.CharField(max_length=255, choices=BANKS, blank=False, default=ALPHABANK)
    date = models.DateTimeField(verbose_name='Дата Курса Валют', default=timezone.now)
    eur_buy = models.FloatField(verbose_name='Покупка EUR', default=1)
    eur_sell = models.FloatField(verbose_name='Продажа EUR', default=1)
    usd_buy = models.FloatField(verbose_name='Покупка USD', default=1)
    usd_sell = models.FloatField(verbose_name='Продажа USD', default=1)
    rur_buy = models.FloatField(verbose_name='Покупка RUR', default=1)
    rur_sell = models.FloatField(verbose_name='Продажа RUR', default=1)

    class Meta:
        pass

    def __str__(self):
        return self.date


class UnAuth(models.Model):
    """для неавторизованных пользователей"""
    ALPHABANK = 'АльфаБанк'
    BELAGROPROMBANK = 'БелАгроПромБанк'
    BELARUSBANK = 'БеларусБанк'

    BANKS = [
        (ALPHABANK, 'Альфабанк'),
        (BELAGROPROMBANK, 'Белагропром'),
        (BELARUSBANK, 'Беларусбанк'),
    ]
    company = models.CharField(max_length=255, choices=BANKS, blank=False, default=ALPHABANK)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, default=1, verbose_name="Продажа USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="Продажа RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="Продажа EUR")

    class Meta:
        pass

    def __str__(self):
        return self.date
