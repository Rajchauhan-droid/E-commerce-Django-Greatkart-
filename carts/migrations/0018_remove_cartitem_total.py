# Generated by Django 3.1 on 2023-11-09 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0017_cartitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total',
        ),
    ]
