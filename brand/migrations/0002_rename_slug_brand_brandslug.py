# Generated by Django 4.2.3 on 2023-11-02 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='slug',
            new_name='brandslug',
        ),
    ]