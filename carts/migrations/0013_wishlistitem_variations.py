# Generated by Django 3.1 on 2023-11-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20231106_1035'),
        ('carts', '0012_auto_20231107_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
