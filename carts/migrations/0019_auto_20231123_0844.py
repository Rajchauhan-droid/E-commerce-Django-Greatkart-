# Generated by Django 3.1 on 2023-11-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0018_remove_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]