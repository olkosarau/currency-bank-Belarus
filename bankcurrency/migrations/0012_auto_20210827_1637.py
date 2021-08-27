# Generated by Django 3.2.6 on 2021-08-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0011_auto_20210827_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unauth',
            name='eur',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Продажа EUR'),
        ),
        migrations.AlterField(
            model_name='unauth',
            name='rur',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Продажа RUR'),
        ),
        migrations.AlterField(
            model_name='unauth',
            name='usd',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Продажа USD'),
        ),
    ]
