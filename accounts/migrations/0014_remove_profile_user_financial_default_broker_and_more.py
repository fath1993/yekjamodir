# Generated by Django 5.0 on 2024-02-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profile_user_financial_default_broker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_financial_default_broker',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_financial_default_broker_id',
            field=models.PositiveIntegerField(default=0, verbose_name='صندوق  مالی پیشفرض'),
        ),
    ]
