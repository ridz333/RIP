# Generated by Django 2.0.5 on 2019-01-12 20:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190112_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен соответсвовать формату: '+79999999999'.", regex='^\\+?7?\\d{10,15}$')]),
        ),
    ]