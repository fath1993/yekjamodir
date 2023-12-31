# Generated by Django 4.2.6 on 2023-10-31 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0002_alter_filegallery_alt_alter_filegallery_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_type', models.CharField(choices=[('بلاگ', 'بلاگ'), ('تلگرام', 'تلگرام'), ('ایتا', 'ایتا'), ('بله', 'بله'), ('آیگپ', 'آیگپ'), ('گپ', 'گپ')], max_length=255, verbose_name='نوع ربات')),
                ('bot_name', models.CharField(max_length=255, verbose_name='نام ربات')),
                ('bot_token', models.CharField(max_length=255, verbose_name='توکن ربات')),
                ('bot_token_belongs_to', models.CharField(max_length=255, verbose_name='توکن ربات متعلق به کیست؟')),
                ('has_access_to_channels', models.CharField(help_text='ادرس شبکه بدون @ جداسازی با ,', max_length=3000, verbose_name='شبکه هایی که دسترسی دارد')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='bot_created_by', to=settings.AUTH_USER_MODEL, verbose_name='کاربر سازنده')),
            ],
            options={
                'verbose_name': 'ربات',
                'verbose_name_plural': 'ربات ها',
            },
        ),
        migrations.CreateModel(
            name='MetaPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_status', models.CharField(blank=True, choices=[('منتشر شده', 'منتشر شده'), ('حذف شده', 'حذف شده'), ('مجدد منتشر شده', 'مجدد منتشر شده'), ('مجدد ویرایش شده', 'مجدد ویرایش شده'), ('زمان بندی شده', 'زمان بندی شده')], editable=False, max_length=255, null=True, verbose_name='message status')),
                ('message_action', models.CharField(blank=True, choices=[('-', '-'), ('حذف', 'حذف'), ('ویرایش', 'ویرایش'), ('انتشار مجدد', 'انتشار مجدد')], max_length=255, null=True, verbose_name='message action')),
                ('date_of_action', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ اجرا')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='زیر عنوان')),
                ('categories', models.CharField(blank=True, max_length=255, null=True, verbose_name='دسته ها')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='کلمات کلیدی')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='محتوا')),
                ('post_view_type', models.CharField(choices=[('simple_text', 'متن ساده'), ('photo_caption', 'عکس + کپشن'), ('file_description', 'فایل + توضیخات')], default='simple_text', max_length=255, verbose_name='نحوه ارسال متا')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
                ('attached_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='metapost_attached_file', to='gallery.filegallery', verbose_name='فایل ضمیمه')),
                ('attached_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='metapost_attached_image', to='gallery.filegallery', verbose_name='عکس ضمیمه')),
                ('bot', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='auto_robots.bot', verbose_name='auto robot')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='metapost_created_by', to=settings.AUTH_USER_MODEL, verbose_name='کاربر سازنده')),
                ('publish_with_bots', models.ManyToManyField(blank=True, related_name='metapost_publish_with_bots', to='auto_robots.bot', verbose_name='انتشار توسط ربات ها')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='metapost_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='کاربر بروز کننده')),
            ],
            options={
                'verbose_name': 'متا',
                'verbose_name_plural': 'متا ها',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TelegramBotHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_url', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='method url')),
                ('message_status', models.CharField(blank=True, choices=[('منتشر شده', 'منتشر شده'), ('حذف شده', 'حذف شده'), ('مجدد منتشر شده', 'مجدد منتشر شده'), ('مجدد ویرایش شده', 'مجدد ویرایش شده'), ('زمان بندی شده', 'زمان بندی شده')], max_length=255, null=True, verbose_name='message status')),
                ('message_action', models.CharField(blank=True, choices=[('-', '-'), ('حذف', 'حذف'), ('ویرایش', 'ویرایش'), ('انتشار مجدد', 'انتشار مجدد')], max_length=255, null=True, verbose_name='message action')),
                ('response_json', models.TextField(blank=True, editable=False, null=True, verbose_name='response json')),
                ('chat_id', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='chat id')),
                ('message_thread_id', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='message thread id')),
                ('text', models.TextField(blank=True, editable=False, null=True, verbose_name='text')),
                ('parse_mode', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='parse mode')),
                ('entities', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='entities')),
                ('disable_web_page_preview', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='disable web page preview')),
                ('disable_notification', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='disable notification')),
                ('protect_content', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='protect content')),
                ('reply_to_message_id', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='reply to message id')),
                ('allow_sending_without_reply', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='allow sending without reply')),
                ('reply_markup', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='reply markup')),
                ('message_id', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='message id')),
                ('inline_message_id', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='inline message id')),
                ('photo_url', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='photo url')),
                ('caption', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='caption')),
                ('caption_entities', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='caption entities')),
                ('has_spoiler', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='has spoiler')),
                ('metapost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_robots.metapost', verbose_name='metapost')),
            ],
            options={
                'verbose_name': 'تاریخچه ربات تلگرام',
                'verbose_name_plural': 'تاریخچه ربات های تلگرام',
            },
        ),
        migrations.CreateModel(
            name='EitaaBotHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='chat id')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('text', models.TextField(blank=True, null=True, verbose_name='text')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='caption')),
                ('metapost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_robots.metapost', verbose_name='metapost')),
            ],
            options={
                'verbose_name': 'تاریخچه ربات ایتا',
                'verbose_name_plural': 'تاریخچه ربات های ایتا',
            },
        ),
    ]
