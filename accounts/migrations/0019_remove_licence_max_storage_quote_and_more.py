# Generated by Django 5.0 on 2024-02-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_licence_max_storage_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licence',
            name='max_storage_quote',
        ),
        migrations.AddField(
            model_name='vipplan',
            name='max_storage_quote',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='حداکثر فضای ذخیره سازی'),
        ),
    ]
