# Generated by Django 5.0 on 2024-06-16 12:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_usernotification_alter_invoice_options_and_more'),
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotification',
            name='notification',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='notification_user_notification', to='tickets.notification', verbose_name='اطلاعیه'),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_user_notification', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
