# Generated by Django 3.1 on 2023-11-18 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20231118_0809'),
        ('store', '0012_auto_20231118_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.sub_category'),
        ),
    ]
