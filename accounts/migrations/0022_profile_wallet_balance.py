# Generated by Django 5.0 on 2024-05-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_invoice_storage_plan_expiry_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wallet_balance',
            field=models.PositiveIntegerField(default=0, verbose_name='اعتبار حساب'),
        ),
    ]
