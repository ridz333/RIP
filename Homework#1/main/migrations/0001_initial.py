# Generated by Django 2.0.5 on 2019-01-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('link', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.AlterIndexTogether(
            name='menu',
            index_together={('id', 'link')},
        ),
    ]