# Generated by Django 3.2.6 on 2021-09-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0015_alter_currencyauthuser_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyauthuser',
            name='company',
            field=models.CharField(choices=[('АльфаБанк', 'АльфаБанк'), ('БелАгроПромБанк', 'БелАгроПромБанк'), ('АльфаБанк', 'АльфаБанк')], max_length=255),
        ),
    ]