# Generated by Django 3.1 on 2023-11-08 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0015_remove_wishlistitem_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishlistItem',
        ),
    ]