from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=17, blank=True)
    photo = models.ImageField(upload_to='static/images/users/%Y', blank=True, verbose_name='Аватарка',
                              default='/static/images/profile_default.png')

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = 'Профили'

    def __str__(self):
        return '{}'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
