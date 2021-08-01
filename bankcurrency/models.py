from django.db import models
from datetime import date

class Company(models.Model):
    name = models.CharField('Банк', max_length=100, blank=True)

    class Meta:
        verbose_name = 'банк'
        verbose_name_plural = 'банки'

class AlfaBank(models.Model):
    """для авторизованных пользователей"""
    company = models.ForeignKey('Company', verbose_name='Банк', on_delete=models.PROTECT, default=1)
    date = models.ForeignKey('Date', verbose_name='Дата', default=date.today, null=True, on_delete=models.PROTECT)
    eur_buy = models.FloatField(verbose_name='Покупка EUR', default=1)
    eur_sell = models.FloatField(verbose_name='Продажа EUR', default=1)
    usd_buy = models.FloatField(verbose_name='Покупка USD', default=1)
    usd_sell = models.FloatField(verbose_name='Продажа USD', default=1)
    rur_buy = models.FloatField(verbose_name='Покупка RUR', default=1)
    rur_sell = models.FloatField(verbose_name='Продажа RUR', default=1)

    class Meta:
        pass

    def __str__(self):
        pass


class Date(models.Model):
    """День, за который предоставляются курсы валют"""
    date = models.DateField(verbose_name='Дата', default=date.today, null=True)

    def __unicode__(self):
        return 'курсы валют за %s' % self.date.strftime('%d.%m.%Y')

    class Meta:
        verbose_name = 'курсы'
        verbose_name_plural = 'курсы валют'


class AlfaBankUnAuth(models.Model):
    """для неавторизованных пользователей"""
    date = models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')
    usd = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="USD")
    rur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="RUR")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="EUR")

    class Meta:
        pass

    def __str__(self):
        pass


