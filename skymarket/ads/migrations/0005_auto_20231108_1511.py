# Generated by Django 3.2.6 on 2023-11-08 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20231108_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
