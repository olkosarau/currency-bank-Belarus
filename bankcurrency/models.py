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
    company = models.CharField(max_length=255, choices=BANKS, blank=False)
    date = models.DateTimeField(verbose_name='Дата Курса Валют', default=timezone.now)
    eur_buy = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Покупка EUR')
    eur_sell = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Продажа EUR')
    usd_buy = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Покупка USD')
    usd_sell = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Продажа USD')
    rur_buy = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Покупка RUR')
    rur_sell = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Продажа RUR')

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
    company = models.CharField(max_length=255, choices=BANKS, blank=False)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Продажа USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Продажа RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Продажа EUR")

    class Meta:
        pass

    def __str__(self):
        return self.date
