# Generated by Django 2.0.5 on 2019-01-12 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(max_length=1500, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='ImagesForBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='None', verbose_name='Изображение')),
                ('blog', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Blog', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения для блогов',
            },
        ),
    ]
