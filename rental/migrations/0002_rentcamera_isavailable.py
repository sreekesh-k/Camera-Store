# Generated by Django 5.0.5 on 2024-05-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentcamera',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
    ]