# Generated by Django 5.0.4 on 2025-04-14 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='adress',
            new_name='address',
        ),
    ]
