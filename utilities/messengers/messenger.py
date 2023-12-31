import time

from custom_logs.models import custom_log
from utilities.messengers.bale import bale_message_handler
from utilities.messengers.eitaa import eitaa_message_handler
from utilities.messengers.telegram_with_proxy import telegram_message_handler


def messenger(metapost):
    if metapost.bot.bot_type == 'بله':  # bale
        bale_message_handler(metapost)
        time.sleep(1)
    elif metapost.bot.bot_type == 'ایتا':  # eitaa
        eitaa_message_handler(metapost)
        time.sleep(1)
    elif metapost.bot.bot_type == 'تلگرام':  # telegram
        telegram_message_handler(metapost)
        time.sleep(1)

