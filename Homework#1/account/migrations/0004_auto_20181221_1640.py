# Generated by Django 2.0.5 on 2018-12-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181221_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='/static/img/profile_default.jpg', upload_to='static/img/users/%Y', verbose_name='Аватарка'),
        ),
    ]
