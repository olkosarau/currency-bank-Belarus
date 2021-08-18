# Generated by Django 3.2.6 on 2021-08-16 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0006_auto_20210813_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('AL', 'Альфабанк'), ('BA', 'Белагро'), ('BB', 'Беларусбанк')], max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата Курса Валют')),
                ('eur_buy', models.FloatField(default=1, verbose_name='Покупка EUR')),
                ('eur_sell', models.FloatField(default=1, verbose_name='Продажа EUR')),
                ('usd_buy', models.FloatField(default=1, verbose_name='Покупка USD')),
                ('usd_sell', models.FloatField(default=1, verbose_name='Продажа USD')),
                ('rur_buy', models.FloatField(default=1, verbose_name='Покупка RUR')),
                ('rur_sell', models.FloatField(default=1, verbose_name='Продажа RUR')),
            ],
        ),
        migrations.CreateModel(
            name='UnAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('AL', 'Альфабанк'), ('BA', 'Белагро'), ('BB', 'Беларусбанк')], default='AL', max_length=255)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')),
                ('usd', models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='Продажа USD')),
                ('rur', models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='Продажа RUR')),
                ('eur', models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='Продажа EUR')),
            ],
        ),
        migrations.DeleteModel(
            name='AlfaBank',
        ),
        migrations.DeleteModel(
            name='AlfaBankUnAuth',
        ),
        migrations.DeleteModel(
            name='BelApb',
        ),
        migrations.DeleteModel(
            name='BelApbUnAuth',
        ),
        migrations.DeleteModel(
            name='BelBank',
        ),
        migrations.DeleteModel(
            name='BelBankUnAuth',
        ),
    ]