# Generated by Django 3.1 on 2023-11-06 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20231106_1035'),
        ('carts', '0009_wishlistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='product_url',
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='product',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
            preserve_default=False,
        ),
    ]
