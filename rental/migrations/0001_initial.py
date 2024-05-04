# Generated by Django 5.0.4 on 2024-05-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=100)),
                ('specifications', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('charge_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
