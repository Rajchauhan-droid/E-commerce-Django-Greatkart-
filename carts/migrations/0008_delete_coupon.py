# Generated by Django 3.1 on 2023-11-06 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_coupon'),
        ('carts', '0007_coupon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='coupon',
        ),
    ]