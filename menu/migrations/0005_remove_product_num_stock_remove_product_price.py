# Generated by Django 4.2.7 on 2023-12-01 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_product_num_stock_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='num_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]