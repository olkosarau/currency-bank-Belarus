# Generated by Django 3.2.6 on 2021-09-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0019_alter_currencyunauthuser_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyauthuser',
            name='company',
            field=models.CharField(choices=[('alfabank', 'alfabank'), ('belagro', 'belagro'), ('belbank', 'belbank')], max_length=255),
        ),
        migrations.AlterField(
            model_name='currencyunauthuser',
            name='company',
            field=models.CharField(choices=[('alfabank', 'alfabank'), ('belagro', 'belagro'), ('belbank', 'belbank')], max_length=255),
        ),
    ]
