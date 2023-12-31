import time

from django.contrib.auth.models import User
from django.test import TestCase

from auto_robots.models import MetaPost, Bot
from calendar_event.views import date_string_to_date_format
from utilities.messengers.bale import bale_message_handler
from utilities.messengers.eitaa import eitaa_message_handler
from utilities.messengers.telegram_with_proxy import telegram_message_handler


def test_send_message(bot_token, action, message_status, metapost_view_type):
    sender = User.objects.get(username='admin')
    telegram_bot = Bot.objects.get(bot_token=bot_token)
    new_metapost = MetaPost.objects.create(
        bot=telegram_bot,
        action=action,
        send_at=date_string_to_date_format(f'1402/01/01/08:56'),
        send_hourly_at=30,
        is_send_hourly_at_active=True,
        send_daily_at=date_string_to_date_format(f'1402/01/01/07:30'),
        is_send_daily_at_active=True,
        send_monthly_at=date_string_to_date_format(f'1402/01/15/07:30'),
        is_send_monthly_at_active=True,
        send_yearly_at=date_string_to_date_format(f'1402/06/15/07:30'),
        is_send_yearly_at_active=True,
        title='پست تست فانکشن عنوان',
        sub_title='پست تست فانکشن زیر عنوان',
        categories='دسته1',
        keywords='کلمه کلیدی1',
        attached_file_link='https://yekjamodir.ir/media/file-gallery/abstraction-pyramid-glass.jpg',
        content='پست تست فانکشن محتوا',
        metapost_view_type=metapost_view_type,
        message_id='1',
        message_status=message_status,
        created_by=sender,
        updated_by=sender,
    )

    if new_metapost.bot.bot_type == 'بله':  # bale
        bale_message_handler(new_metapost)
        time.sleep(1)
    elif new_metapost.bot.bot_type == 'ایتا':  # eitaa
        eitaa_message_handler(new_metapost)
        time.sleep(1)
    elif new_metapost.bot.bot_type == 'تلگرام':  # telegram
        telegram_message_handler(new_metapost)
        time.sleep(1)