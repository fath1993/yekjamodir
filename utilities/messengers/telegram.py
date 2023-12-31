import json
import threading
import time
import asyncio
import requests
import zipfile
import io
from custom_logs.models import custom_log
from yekjamodir.settings import BASE_URL
from social.models import TelegramBotHistory


def telegram_http_send_message_via_get_method(bot, chat_id, text):
    try:
        req = requests.get(
            url=f'https://api.telegram.org/bot{bot.bot_token}/sendMessage?chat_id=' + str(
                chat_id) + '&text=' + str(text))
        custom_log('telegram_http_send_message_via_get_method-> message: ' + str(req.content))
    except Exception as e:
        custom_log('telegram_http_send_message_via_get_method->try/except. err: ' + str(e))


class TelegramHistoryThread(threading.Thread):
    pass


class TelegramSendMessageThread(threading.Thread):
    def __init__(self, bot, chat_id, text, parse_mode, message_thread_id=None,
                 entities=None, disable_web_page_preview=None, disable_notification=None,
                 protect_content=None, reply_to_message_id=None,
                 allow_sending_without_reply=None, reply_markup=None):
        super().__init__()
        self.bot = bot
        self.chat_id = f'{chat_id}'
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
        try:
            url = f'https://api.telegram.org/bot{self.bot.bot_token}/sendMessage'
            data = {
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
            }
            response = requests.post(url, data=data)
        except Exception as e:
            custom_log(f"telegram send message with post failed. err: {str(e)}")
        return


class TelegramForwardMessageThread(threading.Thread):
    def __init__(self, bot, chat_id, text, parse_mode, message_thread_id=None,
                 entities=None, disable_web_page_preview=None, disable_notification=None,
                 protect_content=None, reply_to_message_id=None,
                 allow_sending_without_reply=None, reply_markup=None):
        super().__init__()
        self.bot = bot
        self.chat_id = f'{chat_id}'
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
        try:
            asyncio.run(self.main())
            url = f'https://api.telegram.org/bot{self.bot.bot_token}/sendMessage'
            data = {
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
            }
            response = requests.post(url, data=data)
        except Exception as e:
            custom_log(f"telegram send message with post failed. err: {str(e)}")
        return


def telegram_http_update_message_via_post_method(bot, chat_id, message_id, text, parse_mode,
                                                 inline_message_id=None,
                                                 entities=None, disable_web_page_preview=None, reply_markup=None):
    reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
    destination_url = f'https://api.telegram.org/bot{bot.bot_token}/editMessageText'
    post_data = {
        'url': destination_url,
        'post_auth_code': 'dy89uys85oPds6fg58',
        'data': {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'disable_web_page_preview': disable_web_page_preview,
            'reply_markup': reply_markup,
        },
        'json': '',
    }
    # Create a BytesIO buffer to hold the ZIP file
    zip_buffer = io.BytesIO()

    # Create a ZIP file
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add text data to the ZIP file (example)
        zipf.writestr('post_data.txt', json.dumps(post_data))

    # Reset the buffer position
    zip_buffer.seek(0)

    files = {'zip_file': ('data.zip', zip_buffer)}
    try:
        response = requests.post(reverse_proxy_url, files=files)
        response_message = {
            'status': 'success',
            'status code': response.status_code,
            'response': response.text,
        }
    except Exception as e:
        response_message = {
            'status': 'failed',
            'status code': '0',
            'response': str(e),
        }
    return f'{json.dumps(response_message)}'


def telegram_http_send_photo_via_post_method(bot, chat_id, photo_url, caption, parse_mode,
                                             message_thread_id=None,
                                             caption_entities=None,
                                             has_spoiler=None, disable_notification=None, protect_content=None,
                                             reply_to_message_id=None, allow_sending_without_reply=None,
                                             reply_markup=None, ):
    reverse_proxy_url = 'https://u313.proxy.yekjamodir.ir/request&code=x21uy5sh25Hms66fg58/'
    destination_url = f'https://api.telegram.org/bot{bot.bot_token}/sendPhoto'
    post_data = {
        'url': destination_url,
        'post_auth_code': 'dy89uys85oPds6fg58',
        'data': {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'photo': photo_url,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'reply_to_message_id': reply_to_message_id,
            'allow_sending_without_reply': allow_sending_without_reply,
            'reply_markup': reply_markup,
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
        response_message = {
            'status': 'success',
            'status code': response.status_code,
            'response': response.text,
        }
    except Exception as e:
        response_message = {
            'status': 'failed',
            'status code': '0',
            'response': str(e),
        }
    return f'{json.dumps(response_message)}'


class TelegramSendPhotoThread(threading.Thread):
    def __init__(self, method_url, blog_post, bot, chat_id, parse_mode, text=None, caption=None, photo=None,
                 message_thread_id=None,
                 entities=None, disable_web_page_preview=None, disable_notification=None,
                 protect_content=None, reply_to_message_id=None,
                 allow_sending_without_reply=None, reply_markup=None, caption_entities=None, has_spoiler=None):
        super().__init__()
        self.method_url = method_url
        self.blog_post = blog_post
        self.bot = bot
        self.chat_id = f'{chat_id}'
        self.text = text
        self.caption = caption
        self.caption_entities = caption_entities
        self.photo = photo
        self.has_spoiler = has_spoiler
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
        try:
            if self.method_url == 'editMessageText':
                pass
            elif self.method_url == 'sendPhoto':
                response_from = telegram_http_send_photo_via_post_method(blog_post=self.blog_post,
                                                                         bot_token=self.bot.bot_token,
                                                                         photo=self.photo,
                                                                         chat_id=self.chat_id, caption=self.caption,
                                                                         parse_mode=self.parse_mode,
                                                                         message_thread_id=self.message_thread_id,
                                                                         caption_entities=self.entities,
                                                                         has_spoiler=self.has_spoiler,
                                                                         disable_notification=self.disable_notification,
                                                                         protect_content=self.protect_content,
                                                                         reply_to_message_id=self.reply_to_message_id,
                                                                         allow_sending_without_reply=self.allow_sending_without_reply,
                                                                         reply_markup=self.reply_markup)

                response = json.loads(response_from)
                if response['status'] == 'success':
                    response_message = json.loads(response['response'])
                else:
                    response_message = response['response']

                new_telegram_bot_history = TelegramBotHistory(
                    bot=self.bot,
                    message_status='منتشر شده',
                    message_action='-',
                    created_by=self.blog_post.created_by,

                    method_url='sendPhoto',
                    response_json=response_message,
                    chat_id=self.chat_id,
                    message_thread_id=self.message_thread_id,
                    text='',
                    parse_mode=self.parse_mode,
                    entities='',
                    disable_web_page_preview='',
                    disable_notification=self.disable_notification,
                    protect_content=self.protect_content,
                    reply_to_message_id=self.reply_to_message_id,
                    allow_sending_without_reply=self.allow_sending_without_reply,
                    reply_markup=self.reply_markup,
                    message_id='',
                    inline_message_id='',
                    photo_url=f'{BASE_URL}{self.blog_post.feature_image.url}',
                    caption=self.caption,
                    caption_entities=self.entities,
                    has_spoiler=self.has_spoiler,
                )
                new_telegram_bot_history.save()
        except Exception as e:
            print(str(e))
        return
