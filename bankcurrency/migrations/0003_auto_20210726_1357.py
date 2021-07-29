# Generated by Django 3.2.5 on 2021-07-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0002_auto_20210725_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alfabank',
            options={},
        ),
        migrations.RemoveField(
            model_name='alfabank',
            name='date_upgrade',
        ),
        migrations.RemoveField(
            model_name='alfabank',
            name='price_currency',
        ),
        migrations.AddField(
            model_name='alfabank',
            name='eur',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='EUR'),
        ),
        migrations.AddField(
            model_name='alfabank',
            name='rur',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='RUR'),
        ),
        migrations.AddField(
            model_name='alfabank',
            name='usd',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='USD'),
        ),
        migrations.AlterField(
            model_name='alfabank',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='alfabank',
            name='done',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alfabank',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Валюта'),
        ),
    ]