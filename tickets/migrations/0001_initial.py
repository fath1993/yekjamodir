# Generated by Django 5.0 on 2024-06-16 12:44

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0003_alter_filegallery_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('attachments', models.ManyToManyField(blank=True, to='gallery.filegallery', verbose_name='ضمائم')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_notification', to=settings.AUTH_USER_MODEL, verbose_name='ساخته شده توسط')),
            ],
            options={
                'verbose_name': 'اطلاعیه',
                'verbose_name_plural': 'اطلاعیه ها',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'ایجاد شده'), ('pending', 'در حال بررسی'), ('admin_response', 'پاسخ ادمین'), ('closed', 'بسته شده'), ('owner_response', 'پاسخ داده شده توسط فرستنده'), ('receiver_response', 'پاسخ داده شده توسط گیرنده')], default='created', max_length=255, verbose_name='وضعیت تیکت')),
                ('subject', models.CharField(blank=True, max_length=1024, null=True, verbose_name='موضوع تیکت')),
                ('has_seen_by_owner', models.BooleanField(default=False, verbose_name='دیده شده توسط فرستنده')),
                ('has_seen_by_receiver', models.BooleanField(default=False, verbose_name='دیده شده توسط گیرنده')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_created_by', to=settings.AUTH_USER_MODEL, verbose_name='ساخته شده توسط')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_owner', to=settings.AUTH_USER_MODEL, verbose_name='متعلق به')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_receiver', to=settings.AUTH_USER_MODEL, verbose_name='ارسال شده به')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='بروز شده توسط')),
            ],
            options={
                'verbose_name': 'تیکت',
                'verbose_name_plural': 'تیکت ها',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('attachments', models.ManyToManyField(blank=True, to='gallery.filegallery', verbose_name='ضمائم')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_message', to=settings.AUTH_USER_MODEL, verbose_name='ساخته شده توسط')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_message', to='tickets.ticket', verbose_name='تیکت')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
                'ordering': ['-created_at'],
            },
        ),
    ]
