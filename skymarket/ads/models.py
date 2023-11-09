from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Ad(models.Model):

    title = models.CharField(max_length=50, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='ads/', verbose_name='изображение', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='комментатор', **NULLABLE)
    text = models.TextField(verbose_name='отзыв')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
