# Generated by Django 5.0.6 on 2024-06-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_salescamera_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescamera',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='cameraStore'),
        ),
    ]
