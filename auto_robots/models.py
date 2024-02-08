import time

import jdatetime
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_jalali.db import models as jmodels
from tinymce.models import HTMLField
from gallery.models import FileGallery
from utilities.slug_generator import name_to_url

BOT_TYPE = (('بلاگ', 'بلاگ'), ('تلگرام', 'تلگرام'), ('ایتا', 'ایتا'), ('بله', 'بله'), ('آیگپ', 'آیگپ'), ('گپ', 'گپ'))
ACTION = (('new_send', 'ارسال جدید'), ('republish', 'انتشار مجدد'), ('revise', 'ویرایش'), ('delete', 'حذف'))

MESSAGE_STATUS = (('processing', 'در دست اقدام'), ('sent', 'منتشر شده'), ('queued', 'زمانبندی شده'), ('republished', 'مجدد منتشر شده'), ('revised', 'مجدد ویرایش شده'), ('deleted', 'حذف شده'), ('failed', 'انتشار ناموفق'))
PARS_MODE = (('HTML', 'HTML'), ('MARKDOWN', 'MARKDOWN'))
METAPOST_TYPE = (('simple_text', 'متن ساده'), ('photo', 'عکس + کپشن'), ('video', 'ویدئو + کپشن')
                 , ('audio', 'صوت + کپشن'), ('document', 'فایل + کپشن'))
METAPOST_SEND_AT_TYPE = (('در لحظه یکباره', 'در لحظه یکباره'), ('زمانبندی شده یکباره', 'زمانبندی شده یکباره'), ('روزانه', 'روزانه'),
                         ('هفتگی', 'هفتگی'), ('ماهانه', 'ماهانه'), ('سالانه', 'سالانه'))


class Bot(models.Model):
    bot_type = models.CharField(max_length=255, choices=BOT_TYPE, null=False, blank=False, verbose_name='نوع ربات')
    bot_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام ربات')
    bot_token = models.CharField(max_length=255, null=True, blank=True, verbose_name='توکن ربات')
    bot_token_belongs_to = models.CharField(max_length=255, null=True, blank=True,
                                            verbose_name='توکن ربات متعلق به کیست؟')
    has_access_to_channels = models.CharField(max_length=3000, null=True, blank=True,
                                              verbose_name='شبکه هایی که دسترسی دارد',
                                              help_text='ادرس شبکه بدون @ جداسازی با ,')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, related_name='bot_created_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر سازنده')

    def __str__(self):
        return f'{self.bot_type} | {self.bot_name}'

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'ربات'
        verbose_name_plural = 'ربات ها'

    def save(self, *args, **kwargs):
        if self.has_access_to_channels:
            self.has_access_to_channels = has_access_to_channels_cleaner(self.has_access_to_channels)
        super().save()

    def get_absolute_url(self):
        return reverse('auto_robots:auto-robots-edit-with-id', kwargs={'auto_robot_id': self.id})


def has_access_to_channels_cleaner(text: str):
    text = text.replace('،', ',')
    channels = text.split(',')
    channels_edited = []
    for channel in channels:
        while True:
            if channel[0] == ' ':
                channel = channel[1:]
            else:
                break
        while True:
            if channel[-1] == ' ':
                channel = channel[:-2]
            else:
                break
        channels_edited.append(channel)
    return ','.join(channels_edited)


class MetaPost(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, null=False, blank=False, verbose_name='ربات')
    action = models.CharField(max_length=255, choices=ACTION, null=False, blank=False, verbose_name='عملیات')
    send_at_type = models.CharField(max_length=255, choices=METAPOST_SEND_AT_TYPE, null=False, blank=False, verbose_name='نوع ارسال متاپست')
    send_at_date_time = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ و زمان ارسال')
    message_status = models.CharField(max_length=255, choices=MESSAGE_STATUS, null=True, blank=True,
                                      editable=True, verbose_name='وضعیت')

    title = models.CharField(max_length=1000, null=False, blank=False, verbose_name='عنوان')
    sub_title = models.CharField(max_length=1000, null=True, blank=True, verbose_name='زیر عنوان')
    categories = models.CharField(max_length=3000, null=True, blank=True, verbose_name='دسته ها')
    keywords = models.CharField(max_length=3000, null=True, blank=True, verbose_name='کلمات کلیدی')
    attached_file_link = models.CharField(max_length=3000, null=True, blank=True, verbose_name='لینک فایل ضمیمه')
    content = HTMLField(null=True, blank=True, verbose_name='محتوا')
    metapost_view_type = models.CharField(max_length=255, default='simple_text', choices=METAPOST_TYPE, null=False,
                                          blank=False,
                                          verbose_name='نحوه ارسال متا')
    message_id = models.CharField(default=0, max_length=255, null=False, blank=False, editable=False,
                                  verbose_name='message id')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='metapost_created_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر سازنده')
    updated_by = models.ForeignKey(User, related_name='metapost_updated_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر بروز کننده')

    def __str__(self):
        return str(self.id) + ' | ' + self.title

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "متا"
        verbose_name_plural = "متا ها"

    def get_absolute_url(self):
        return reverse('auto_robots:metapost-edit-with-metapost-id', kwargs={'metapost_id': self.id})


class MetapostHistory(models.Model):
    metapost = models.ForeignKey(MetaPost, on_delete=models.CASCADE, null=False, blank=False, verbose_name='metapost')
    response_message = models.TextField(null=False, blank=False, verbose_name='پیام بازگشتی')
    chat_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='chat id')
    message_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='message id')

    class Meta:
        verbose_name = 'تاریخچه ارسال متا'
        verbose_name_plural = 'تاریخچه ارسال متا ها'
