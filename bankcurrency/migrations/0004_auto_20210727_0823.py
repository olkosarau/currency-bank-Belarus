# Generated by Django 3.2.5 on 2021-07-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0003_auto_20210726_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alfabank',
            name='date',
        ),
        migrations.AlterField(
            model_name='alfabank',
            name='title',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата Курса Валют'),
        ),
    ]