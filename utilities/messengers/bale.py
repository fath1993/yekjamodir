import json
import threading
import requests
from bs4 import BeautifulSoup
from auto_robots.models import MetapostHistory
from subscription.templatetags.subscription_tag import profile_withdraw_message_price
from yekjamodir.settings import BASE_URL


def bale_http_send_message_via_post_method(metapost, bot_token, chat_id, text, reply_to_message_id=None,
                                           reply_markup=None):
    BaleHttpSendMessageViaPostMethodThread(metapost=metapost, bot_token=bot_token, chat_id=chat_id, text=text,
                                           reply_to_message_id=reply_to_message_id, reply_markup=reply_markup).start()


class BaleHttpSendMessageViaPostMethodThread(threading.Thread):
    def __init__(self, metapost, bot_token, chat_id, text, reply_to_message_id=None, reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.text = text
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup

    def run(self):
        url = f'https://tapi.bale.ai/bot{self.bot_token}/sendMessage'
        data = {
            'chat_id': f'@{self.chat_id}',
            'text': self.text,
            'reply_to_message_id': self.reply_to_message_id,
            'reply_markup': self.reply_markup,
        }
        try:
            response = requests.post(url=url, data=data)
            response_message = response.text
            message_id = json.loads(response_message)['result']['message_id']
        except Exception as e:
            message_id = 0
            response_message = str(e)
        self.metapost.message_id = message_id
        self.metapost.save()
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                       chat_id=self.chat_id, message_id=message_id)
        return print(response_message)


def bale_http_update_message_via_post_method(metapost, bot_token, chat_id, text, reply_markup=None):
    BaleHttpUpdateMessageViaPostMethod(metapost=metapost, bot_token=bot_token, chat_id=chat_id,
                                       text=text, reply_markup=reply_markup).start()


class BaleHttpUpdateMessageViaPostMethod(threading.Thread):
    def __init__(self, metapost, bot_token, chat_id, text, reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.text = text
        self.reply_markup = reply_markup

    def run(self):
        url = f'https://tapi.bale.ai/bot{self.bot_token}/EditMessageText'
        data = {
            "chat_id": f"@{self.chat_id}",
            "message_id": self.metapost.message_id,
            "text": self.text,
            "reply_markup": self.reply_markup,
        }
        try:
            response = requests.post(url=url, data=data)
            response_message = response.text
        except Exception as e:
            response_message = str(e)
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                       chat_id=self.chat_id,
                                       message_id=self.metapost.message_id)
        return print(response_message)


def bale_http_delete_message_via_post_method(metapost, bot_token, chat_id):
    BaleHttpDeleteMessageViaPostMethod(metapost=metapost, bot_token=bot_token, chat_id=chat_id).start()


class BaleHttpDeleteMessageViaPostMethod(threading.Thread):
    def __init__(self, metapost, bot_token, chat_id):
        super().__init__()
        self.metapost = metapost
        self.bot_token = bot_token
        self.chat_id = chat_id

    def run(self):
        url = f'https://tapi.bale.ai/bot{self.bot_token}/deletemessage'
        data = {
            'chat_id': f'@{self.chat_id}',
            'message_id': self.metapost.message_id,
        }
        try:
            response = requests.post(url=url, data=data)
            response_message = response.text
        except Exception as e:
            response_message = str(e)
        self.metapost.message_id = 0
        self.metapost.save()
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                       chat_id=self.chat_id,
                                       message_id=self.metapost.message_id)
        return print(response_message)


def bale_http_send_media_via_post_method(metapost, bot_token, chat_id, media_type, media_url, caption,
                                         reply_to_message_id=None):
    BaleHttpSendMediaViaPostMethod(metapost=metapost, bot_token=bot_token, chat_id=chat_id, media_type=media_type,
                                   media_url=media_url, caption=caption,
                                   reply_to_message_id=reply_to_message_id).start()


class BaleHttpSendMediaViaPostMethod(threading.Thread):
    def __init__(self, metapost, bot_token, chat_id, media_type, media_url, caption, reply_to_message_id=None):
        super().__init__()
        self.metapost = metapost
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.media_type = media_type
        self.media_url = media_url
        self.caption = caption
        self.reply_to_message_id = reply_to_message_id

    def run(self):
        url = f'https://tapi.bale.ai/bot{self.bot_token}/Send{self.media_type}'
        data = {
            "chat_id": f'@{self.chat_id}',
            f"{self.media_type}": self.media_url,
            "caption": self.caption,
            "reply_to_message_id": self.reply_to_message_id,
        }
        try:
            response = requests.post(url=url, data=data)
            response_message = response.text
            message_id = json.loads(response_message)['result']['message_id']
        except Exception as e:
            message_id = 0
            response_message = str(e)
        self.metapost.message_id = message_id
        self.metapost.save()
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                       chat_id=self.chat_id,
                                       message_id=message_id)
        return print(response_message)


def bale_message_handler(metapost):
    channels = metapost.bot.has_access_to_channels.split(',')
    soup = BeautifulSoup(metapost.content)
    content = ''
    if metapost.content:
        content += soup.text
        content += '\n'
    if metapost.categories:
        categories = metapost.categories.split(',')
        new_cat_list = []
        for cat in categories:
            new_cat_list.append(f'#{cat.replace(" ", "_")}')
        content += ' '.join(new_cat_list)
        content += '\n'
    if metapost.keywords:
        keywords = metapost.keywords.split(',')
        new_key_list = []
        for key in keywords:
            new_key_list.append(f'#{key.replace(" ", "_")}')
        content += ' '.join(new_key_list)
        content += '\n'

    for channel in channels:
        if metapost.action == 'new_send':
            profile_withdraw_message_price(metapost.created_by.profile_user)
            if metapost.metapost_view_type == 'simple_text':
                bale_http_send_message_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                       chat_id=channel, text=content)
            else:
                if metapost.metapost_view_type == 'photo':
                    media_url = f'{metapost.attached_file_link}'
                else:
                    media_url = f'{metapost.attached_file_link}'
                bale_http_send_media_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                     caption=content,
                                                     chat_id=channel, media_type=metapost.metapost_view_type,
                                                     media_url=media_url)
        elif metapost.action == 'republish':
            bale_http_delete_message_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                     chat_id=channel)
            if metapost.metapost_view_type == 'simple_text':
                bale_http_send_message_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                       chat_id=channel, text=content)
            else:
                if metapost.metapost_view_type == 'photo':
                    media_url = f'{metapost.attached_file_link}'
                else:
                    media_url = f'{metapost.attached_file_link}'
                bale_http_send_media_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                     caption=content,
                                                     chat_id=channel, media_type=metapost.metapost_view_type,
                                                     media_url=media_url)
        elif metapost.action == 'revise':
            if metapost.metapost_view_type == 'simple_text':
                bale_http_update_message_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                         chat_id=channel, text=content)
            else:
                print('تعریف نشده')
        elif metapost.action == 'delete':
            bale_http_delete_message_via_post_method(metapost=metapost, bot_token=metapost.bot.bot_token,
                                                     chat_id=channel)


'''  samples
                ارسال متن ساده

        bale_http_send_message_via_post_method('628885016:R8b4MGvBomNvTEQdXcgtayycOKGQaJeRiGO7oNS3',
                                               'amir3165', 'این یک پیام تستی است', reply_to_message_id=None, reply_markup=None)


                اصلاح متن ساده

        bale_http_update_message_via_post_method('628885016:R8b4MGvBomNvTEQdXcgtayycOKGQaJeRiGO7oNS3',
                                                 'amir3165', 7, 'این یک اصلاحیه 2 پیام تستی است', reply_markup=None)


                حذف پست

        bale_http_delete_message_via_post_method('628885016:R8b4MGvBomNvTEQdXcgtayycOKGQaJeRiGO7oNS3',
                                                 'amir3165', 15)


        ارسال انواع فایل - موارد قابل انتخاب: photo - video - document - audio

        bale_http_send_media_via_post_method('628885016:R8b4MGvBomNvTEQdXcgtayycOKGQaJeRiGO7oNS3',
                                             'amir3165', 'audio',
                                             'https://yekjamodir.ir/media/file-gallery/%D9%86%D8%A7%D9%87%D8%A7%D8%B1-%DA%86%D9%87%D8%A7%D8%B1%D8%B4%D9%86%D8%A8%D9%87-3-%D8%A2%D8%A8%D8%A7%D9%86.jpg',
                                             'این یک تصویر متن دار است', reply_to_message_id=None)
'''
