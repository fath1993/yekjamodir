# Generated by Django 5.0 on 2024-05-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_profile_wallet_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='vip_plan',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('واریز به حساب', 'واریز به حساب'), ('برداشت از حساب', 'برداشت از حساب')], default='برداشت', max_length=255, verbose_name='نوع صورت حساب'),
        ),
    ]
