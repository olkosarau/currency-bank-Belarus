# Generated by Django 3.2.5 on 2021-08-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0002_alter_alfabank_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='BelApb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=1, verbose_name='Дата')),
                ('eur_buy', models.FloatField(default=1, verbose_name='Покупка EUR')),
                ('eur_sell', models.FloatField(default=1, verbose_name='Продажа EUR')),
                ('usd_buy', models.FloatField(default=1, verbose_name='Покупка USD')),
                ('usd_sell', models.FloatField(default=1, verbose_name='Продажа USD')),
                ('rur_buy', models.FloatField(default=1, verbose_name='Покупка RUR')),
                ('rur_sell', models.FloatField(default=1, verbose_name='Продажа RUR')),
            ],
        ),
        migrations.CreateModel(
            name='BelApbUnAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют')),
                ('usd', models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='USD')),
                ('rur', models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='RUR')),
                ('eur', models.DecimalField(decimal_places=2, default='1', max_digits=5, verbose_name='EUR')),
            ],
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'банк'},
        ),
        migrations.AlterField(
            model_name='alfabank',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bankcurrency.company', verbose_name='АльфаБанк'),
        ),
        migrations.AddField(
            model_name='belapb',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bankcurrency.company', verbose_name='БелАгроПромБанк'),
        ),
    ]