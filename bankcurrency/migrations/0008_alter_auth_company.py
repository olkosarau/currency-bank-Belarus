# Generated by Django 3.2.6 on 2021-08-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcurrency', '0007_auto_20210816_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='company',
            field=models.CharField(choices=[('alfabank', 'Альфабанк'), ('belagrobank', 'Белагро'), ('belarusbank', 'Беларусбанк')], max_length=255),
        ),
    ]