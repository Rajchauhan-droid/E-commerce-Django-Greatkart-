# Generated by Django 3.1 on 2023-11-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0020_auto_20231123_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]