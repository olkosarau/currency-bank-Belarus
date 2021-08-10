from django.db import models
from django.utils import timezone
import pytz


class Company(models.Model):
    name = models.CharField('Банк', max_length=100, blank=True)

    class Meta:
        verbose_name = 'банк'

    def __str__(self):
        return self.name


class AlfaBank(models.Model):
    """для авторизованных пользователей"""
    company = models.ForeignKey('Company', verbose_name='АльфаБанк', on_delete=models.PROTECT, null=True)
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
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


class AlfaBankUnAuth(models.Model):
    """для неавторизованных пользователей"""
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="EUR")

    class Meta:
        pass

    def __str__(self):
        return self.date


class BelApb(models.Model):
    """для авторизованных пользователей"""
    company = models.ForeignKey('Company', verbose_name='БелАгроПромБанк', on_delete=models.PROTECT, null=True)
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
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


class BelApbUnAuth(models.Model):
    """для неавторизованных пользователей"""
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="EUR")

    class Meta:
        pass

    def __str__(self):
        return self.date


class BelBank(models.Model):
    """для авторизованных пользователей"""
    company = models.ForeignKey('Company', verbose_name='ПриорБанк', on_delete=models.PROTECT, null=True)
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
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


class BelBankUnAuth(models.Model):
    """для неавторизованных пользователей"""
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="EUR")

    class Meta:
        pass

    def __str__(self):
        return self.date