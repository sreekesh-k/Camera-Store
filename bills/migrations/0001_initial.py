# Generated by Django 5.0.4 on 2024-05-04 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0002_rename_camera_salescamera'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sales_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.salescamera')),
            ],
        ),
    ]