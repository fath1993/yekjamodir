import json
import threading
import requests
import zipfile
import io

from bs4 import BeautifulSoup

from auto_robots.models import MetapostHistory
from yekjamodir.settings import BASE_URL


class TelegramHttpSendMessageThread(threading.Thread):
    def __init__(self, metapost, chat_id, text, parse_mode, message_thread_id=None,
                 entities=None, disable_web_page_preview=None, disable_notification=None,
                 protect_content=None, reply_to_message_id=None,
                 allow_sending_without_reply=None, reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.chat_id = f'@{chat_id}'
        self.text = text
        self.parse_mode = parse_mode
        self.message_thread_id = message_thread_id
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup

    def run(self):
        reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
        destination_url = f'https://api.telegram.org/bot{self.metapost.bot.bot_token}/sendMessage'
        post_data = {
            'url': destination_url,
            'post_auth_code': 'dy89uys85oPds6fg58',
            'data': {
                'chat_id': self.chat_id,
                'message_thread_id': self.message_thread_id,
                'text': self.text,
                'parse_mode': self.parse_mode,
                'entities': self.entities,
                'disable_web_page_preview': self.disable_web_page_preview,
                'disable_notification': self.disable_notification,
                'protect_content': self.protect_content,
                'reply_to_message_id': self.reply_to_message_id,
                'allow_sending_without_reply': self.allow_sending_without_reply,
                'reply_markup': self.reply_markup,
            },
            'json': '',
        }
        # Create a BytesIO buffer to hold the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('post_data.txt', json.dumps(post_data))

        # Reset the buffer position
        zip_buffer.seek(0)

        files = {'zip_file': ('data.zip', zip_buffer)}
        try:
            response = requests.post(reverse_proxy_url, files=files)
            response_message = response.text
            message_id = json.loads(json.loads(response_message)['response_message'])['result']['message_id']
        except Exception as e:
            message_id = 0
            response_message = str(e)
        self.metapost.message_id = message_id
        self.metapost.save()
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                          chat_id=self.chat_id,
                                          message_id=message_id)
        return


class TelegramEditMessageTextThread(threading.Thread):
    def __init__(self, metapost, chat_id, text, parse_mode, inline_message_id=None,
                 entities=None, disable_web_page_preview=None, reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.chat_id = f'@{chat_id}'
        self.text = text
        self.parse_mode = parse_mode
        self.inline_message_id = inline_message_id
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview
        self.reply_markup = reply_markup

    def run(self):
        reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
        destination_url = f'https://api.telegram.org/bot{self.metapost.bot.bot_token}/editMessageText'
        post_data = {
            'url': destination_url,
            'post_auth_code': 'dy89uys85oPds6fg58',
            'data': {
                'chat_id': self.chat_id,
                'message_id': self.metapost.message_id,
                'text': self.text,
                'parse_mode': self.parse_mode,
                'inline_message_id': self.inline_message_id,
                'entities': self.entities,
                'disable_web_page_preview': self.disable_web_page_preview,
                'reply_markup': self.reply_markup,
            },
            'json': '',
        }
        # Create a BytesIO buffer to hold the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('post_data.txt', json.dumps(post_data))

        # Reset the buffer position
        zip_buffer.seek(0)

        files = {'zip_file': ('data.zip', zip_buffer)}
        try:
            response = requests.post(reverse_proxy_url, files=files)
            response_message = response.text
        except Exception as e:
            response_message = str(e)
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                          chat_id=self.chat_id,
                                          message_id=self.metapost.message_id)
        return


class TelegramEditMessageCaptionThread(threading.Thread):
    def __init__(self, metapost, chat_id, caption, parse_mode, inline_message_id=None,
                 caption_entities=None, reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.chat_id = f'@{chat_id}'
        self.caption = caption
        self.parse_mode = parse_mode
        self.inline_message_id = inline_message_id
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup

    def run(self):
        reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
        destination_url = f'https://api.telegram.org/bot{self.metapost.bot.bot_token}/editMessageCaption'
        post_data = {
            'url': destination_url,
            'post_auth_code': 'dy89uys85oPds6fg58',
            'data': {
                'chat_id': self.chat_id,
                'message_id': self.metapost.message_id,
                'caption': self.caption,
                'parse_mode': self.parse_mode,
                'inline_message_id': self.inline_message_id,
                'caption_entities': self.caption_entities,
                'reply_markup': self.reply_markup,
            },
            'json': '',
        }
        # Create a BytesIO buffer to hold the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('post_data.txt', json.dumps(post_data))

        # Reset the buffer position
        zip_buffer.seek(0)

        files = {'zip_file': ('data.zip', zip_buffer)}
        try:
            response = requests.post(reverse_proxy_url, files=files)
            response_message = response.text
        except Exception as e:
            response_message = str(e)
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                          chat_id=self.chat_id,
                                          message_id=self.metapost.message_id)
        return


class TelegramEditMessageMediaThread(threading.Thread):
    def __init__(self, metapost, chat_id, media, inline_message_id=None, reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.chat_id = f'@{chat_id}'
        self.media = media
        self.inline_message_id = inline_message_id
        self.reply_markup = reply_markup

    def run(self):
        reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
        destination_url = f'https://api.telegram.org/bot{self.metapost.bot.bot_token}/editMessageMedia'
        post_data = {
            'url': destination_url,
            'post_auth_code': 'dy89uys85oPds6fg58',
            'data': {
                'chat_id': self.chat_id,
                'message_id': self.metapost.message_id,
                'media': self.media,
                'inline_message_id': self.inline_message_id,
                'reply_markup': self.reply_markup,
            },
            'json': '',
        }
        # Create a BytesIO buffer to hold the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('post_data.txt', json.dumps(post_data))

        # Reset the buffer position
        zip_buffer.seek(0)

        files = {'zip_file': ('data.zip', zip_buffer)}
        try:
            response = requests.post(reverse_proxy_url, files=files)
            response_message = response.text
        except Exception as e:
            response_message = str(e)
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                          chat_id=self.chat_id,
                                          message_id=self.metapost.message_id)
        return


class TelegramHttpSendMediaThread(threading.Thread):
    def __init__(self, metapost, chat_id, media_type, media_url, caption, parse_mode,
                 message_thread_id=None,
                 caption_entities=None,
                 has_spoiler=None, disable_notification=None, protect_content=None,
                 reply_to_message_id=None, allow_sending_without_reply=None,
                 reply_markup=None):
        super().__init__()
        self.metapost = metapost
        self.chat_id = f'@{chat_id}'
        self.media_type = media_type
        self.media_url = media_url
        self.caption = caption
        self.message_thread_id = message_thread_id
        self.caption_entities = caption_entities
        self.has_spoiler = has_spoiler
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup

    def run(self):
        reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
        destination_url = f'https://api.telegram.org/bot{self.metapost.bot.bot_token}/send{str(self.media_type).capitalize()}'
        post_data = {
            'url': destination_url,
            'post_auth_code': 'dy89uys85oPds6fg58',
            'data': {
                'chat_id': self.chat_id,
                'message_thread_id': self.message_thread_id,
                f'{self.media_type}': self.media_url,
                'caption': self.caption,
                'parse_mode': self.parse_mode,
                'caption_entities': self.caption_entities,
                'has_spoiler': self.has_spoiler,
                'disable_notification': self.disable_notification,
                'protect_content': self.protect_content,
                'reply_to_message_id': self.reply_to_message_id,
                'allow_sending_without_reply': self.allow_sending_without_reply,
                'reply_markup': self.reply_markup,
            },
            'json': '',
        }
        # Create a BytesIO buffer to hold the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add text data to the ZIP file (example)
            zipf.writestr('post_data.txt', json.dumps(post_data))

            # # Add binary data (e.g., image) to the ZIP file (example)
            # with open('image.jpg', 'rb') as image_file:
            #     image_data = image_file.read()
            #     zipf.writestr('image.jpg', image_data)

        # Reset the buffer position
        zip_buffer.seek(0)

        files = {'zip_file': ('data.zip', zip_buffer)}
        try:
            response = requests.post(reverse_proxy_url, files=files)
            response_message = response.text
            message_id = json.loads(json.loads(response_message)['response_message'])['result']['message_id']
        except Exception as e:
            message_id = 0
            response_message = str(e)
        self.metapost.message_id = message_id
        self.metapost.save()
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                          chat_id=self.chat_id,
                                          message_id=message_id)
        return


class TelegramDeleteMessageThread(threading.Thread):
    def __init__(self, metapost, chat_id):
        super().__init__()
        self.metapost = metapost
        self.chat_id = f'@{chat_id}'

    def run(self):
        reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
        destination_url = f'https://api.telegram.org/bot{self.metapost.bot.bot_token}/deleteMessage'
        post_data = {
            'url': destination_url,
            'post_auth_code': 'dy89uys85oPds6fg58',
            'data': {
                'chat_id': self.chat_id,
                'message_id': self.metapost.message_id,
            },
            'json': '',
        }
        # Create a BytesIO buffer to hold the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('post_data.txt', json.dumps(post_data))

        # Reset the buffer position
        zip_buffer.seek(0)

        files = {'zip_file': ('data.zip', zip_buffer)}
        try:
            response = requests.post(reverse_proxy_url, files=files)
            response_message = response.text
            message_id = 0
        except Exception as e:
            message_id = 0
            response_message = str(e)
        print(response_message)
        self.metapost.message_id = message_id
        self.metapost.save()
        MetapostHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                          chat_id=self.chat_id,
                                          message_id=message_id)
        return


def telegram_send_message(metapost, chat_id, text, parse_mode, message_thread_id=None,
                          entities=None, disable_web_page_preview=None, disable_notification=None,
                          protect_content=None, reply_to_message_id=None,
                          allow_sending_without_reply=None, reply_markup=None):
    TelegramHttpSendMessageThread(metapost=metapost, chat_id=chat_id, text=text, parse_mode=parse_mode,
                                  message_thread_id=message_thread_id,
                                  entities=entities, disable_web_page_preview=disable_web_page_preview,
                                  disable_notification=disable_notification, protect_content=protect_content,
                                  reply_to_message_id=reply_to_message_id,
                                  allow_sending_without_reply=allow_sending_without_reply,
                                  reply_markup=reply_markup).start()


def telegram_edit_message_text(metapost, chat_id, text, parse_mode, inline_message_id=None,
                               entities=None, disable_web_page_preview=None, reply_markup=None):
    TelegramEditMessageTextThread(metapost=metapost, chat_id=chat_id, text=text,
                                  parse_mode=parse_mode, inline_message_id=inline_message_id, entities=entities,
                                  disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup).start()


def telegram_edit_message_caption(metapost, chat_id, caption, parse_mode, inline_message_id=None,
                                  caption_entities=None, reply_markup=None):
    TelegramEditMessageCaptionThread(metapost=metapost, chat_id=chat_id, caption=caption,
                                     parse_mode=parse_mode, inline_message_id=inline_message_id,
                                     caption_entities=caption_entities,
                                     reply_markup=reply_markup).start()


def telegram_edit_message_media(metapost, chat_id, message_id, media, inline_message_id=None, reply_markup=None):
    TelegramEditMessageMediaThread(metapost=metapost, chat_id=chat_id, media=media,
                                   inline_message_id=inline_message_id, reply_markup=reply_markup).start()


def telegram_send_media(metapost, chat_id, media_type, media_url, caption, parse_mode,
                        message_thread_id=None,
                        caption_entities=None,
                        has_spoiler=None, disable_notification=None, protect_content=None,
                        reply_to_message_id=None, allow_sending_without_reply=None,
                        reply_markup=None):
    TelegramHttpSendMediaThread(metapost=metapost, chat_id=chat_id, media_type=media_type, media_url=media_url,
                                caption=caption, parse_mode=parse_mode, message_thread_id=message_thread_id,
                                caption_entities=caption_entities, has_spoiler=has_spoiler,
                                disable_notification=disable_notification, protect_content=protect_content,
                                reply_to_message_id=reply_to_message_id,
                                allow_sending_without_reply=allow_sending_without_reply,
                                reply_markup=reply_markup).start()


def telegram_delete_message(metapost, chat_id):
    TelegramDeleteMessageThread(metapost=metapost, chat_id=chat_id).start()


def telegram_message_handler(metapost):
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
            if metapost.metapost_view_type == 'simple_text':
                telegram_send_message(metapost, chat_id=channel, text=content, parse_mode='HTML')
            else:
                telegram_send_media(metapost=metapost, chat_id=channel, media_type=metapost.metapost_view_type,
                                    media_url=metapost.attached_file_link, caption=content, parse_mode='HTML')
        elif metapost.action == 'republish':
            telegram_delete_message(metapost=metapost, chat_id=channel)
            if metapost.metapost_view_type == 'simple_text':
                telegram_send_message(metapost, chat_id=channel, text=content, parse_mode='HTML')
            else:
                telegram_send_media(metapost=metapost, chat_id=channel, media_type=metapost.metapost_view_type,
                                    media_url=metapost.attached_file_link, caption=content, parse_mode='HTML')
        elif metapost.action == 'revise':
            if metapost.metapost_view_type == 'simple_text':
                telegram_edit_message_text(metapost=metapost, chat_id=channel, text=content, parse_mode='HTML')
            else:
                telegram_edit_message_caption(metapost=metapost, chat_id=channel, caption=content, parse_mode='HTML')
        elif metapost.action == 'delete':
            telegram_delete_message(metapost=metapost, chat_id=channel)
