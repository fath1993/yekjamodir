# Generated by Django 5.0 on 2024-06-18 14:19

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemThreadIsActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='بروز شده در')),
            ],
            options={
                'verbose_name': 'پردازش موازی سیستم',
                'verbose_name_plural': 'پردازش موازی سیستم',
            },
        ),
    ]
