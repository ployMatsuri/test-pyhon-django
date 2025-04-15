# Generated by Django 5.0.4 on 2025-04-15 02:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_rename_adress_school_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='school',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
