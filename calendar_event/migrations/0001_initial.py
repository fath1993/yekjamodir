# Generated by Django 4.2.6 on 2023-11-12 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, verbose_name='رویداد')),
                ('event_description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('start_date', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ شروع رویداد')),
                ('end_date', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ پایان رویداد')),
                ('remind_me_at', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='یاداوری یک باره')),
                ('remind_me_hourly_at', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='یاداوری ساعتی')),
                ('remin_me_daily_at', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='یاداوری روزانه')),
                ('remind_me_monthly_at', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='یاداوری ماهانه')),
                ('remind_me_yearly_at', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='یاداوری سالانه')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='custom_event_created_by', to=settings.AUTH_USER_MODEL, verbose_name='کاربر سازنده')),
            ],
            options={
                'verbose_name': 'رویداد',
                'verbose_name_plural': 'رویداد ها',
            },
        ),
    ]
