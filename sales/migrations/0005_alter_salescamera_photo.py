# Generated by Django 5.0.6 on 2024-06-27 16:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_salescamera_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescamera',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
