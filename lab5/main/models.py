from django.db import models
from django.urls import reverse

class Main(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование:")
    description = models.CharField(max_length=255, verbose_name="Описание", blank=True)
    slug = models.SlugField(unique=True, verbose_name="Адрес на сайте:")
    image = models.ImageField(upload_to='main/static/images', verbose_name="Фото")

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse("main:model",
                       args=[self.id, self.slug])

    def __str__(self):
        return "Статья: {0}".format(self.title)
