# Generated by Django 3.2.6 on 2023-11-07 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ads/', verbose_name='изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время публикации')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad', verbose_name='объявление')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='комментатор')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
    ]
