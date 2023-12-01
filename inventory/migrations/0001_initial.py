# Generated by Django 4.2.7 on 2023-12-01 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0005_remove_product_num_stock_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_price', models.PositiveBigIntegerField()),
                ('num_stock', models.PositiveIntegerField(default=0)),
                ('threshold_low_stack', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockrecords', to='menu.product')),
            ],
        ),
    ]
