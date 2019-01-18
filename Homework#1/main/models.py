from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1500, verbose_name='Текст', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def display_my_safefield(self):
        return mark_safe(self.description)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return "Блог: {}".format(self.title)

class ImagesForBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Изображения', blank=True)
    image = models.ImageField(upload_to='static/images/blogs/%m', verbose_name='Изображение')

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображения для блогов"

    def __str__(self):
        return "Изоброжения для {}".format(self.blog.title)

class CommentsForBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Комментарии', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Комментатор')
    text = models.TextField(max_length=800, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "Комментарии для {}".format(self.blog.title)