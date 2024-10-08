# Generated by Django 4.2.2 on 2023-10-25 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckSmsValidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12, verbose_name='شماره موبایل')),
                ('pass_code', models.CharField(max_length=12, verbose_name='رمز مرتبط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': '2 - تایید 2 مرحله ای',
                'verbose_name_plural': '2 - تایید 2 مرحله ای',
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone_number', models.CharField(blank=True, help_text='شماره موبایل با فرمت 09xx xxxxxxx', max_length=255, null=True, verbose_name='شماره موبایل')),
                ('biography', models.CharField(blank=True, max_length=255, null=True, verbose_name='درباره من')),
                ('is_employee', models.BooleanField(default=False, verbose_name='آیا این کاربر کارمند است؟')),
                ('is_blog_admin', models.BooleanField(default=False, help_text='پست های این کاربر بدون بررسی منتشر میگردد', verbose_name='آیا این کاربر ادمین کل بلاگ است؟')),
                ('profile_pic', models.ImageField(blank=True, verbose_name='عکس پروفایل')),
                ('maximum_storage_quota', models.PositiveIntegerField(default=500, help_text='مگابایت', verbose_name='حداکثر فضای ذخیره سازی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': '1 - پروفایل',
                'verbose_name_plural': '1 - پروفایل',
            },
        ),
    ]
