# Generated by Django 5.0 on 2024-05-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenceSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_licence', models.PositiveIntegerField(default=2000, verbose_name='هزینه روزانه لایسنس حسابداری - تومان')),
                ('warehouse_licence', models.PositiveIntegerField(default=2000, verbose_name='هزینه روزانه لایسنس انبار داری - تومان')),
                ('social_licence', models.PositiveIntegerField(default=2000, verbose_name='هزینه روزانه لایسنس شبکه های اجتماعی - تومان')),
                ('blog_licence', models.PositiveIntegerField(default=2000, verbose_name='هزینه روزانه لایسنس بلاگ - تومان')),
                ('automation_licence', models.PositiveIntegerField(default=2000, verbose_name='هزینه روزانه لایسنس اتوماسیون - تومان')),
                ('send_message', models.PositiveIntegerField(default=100, verbose_name='هزینه ارسال هر پیام - تومان')),
            ],
            options={
                'verbose_name': 'تنظیمات اشتراک',
                'verbose_name_plural': 'تنظیمات اشتراک',
            },
        ),
    ]
