import json
import os
import threading

import requests
from bs4 import BeautifulSoup
from django.contrib.sites.models import Site
from django.core.files.base import ContentFile

from auto_robots.models import EitaaBotHistory
from yekjamodir.settings import BASE_URL


def eitaa_send_simple_text(metapost, chat_id, title, text):
    EitaaSendSimpleTextThread(metapost=metapost, chat_id=chat_id, title=title, text=text).start()


class EitaaSendSimpleTextThread(threading.Thread):
    def __init__(self, metapost, chat_id, title, text):
        super().__init__()
        self.metapost = metapost
        self.chat_id = chat_id
        self.title = title
        self.text = text

    def run(self):
        data = {
            'chat_id': self.chat_id,
            'title': self.title,
            'text': self.text,
        }

        url = f'https://eitaayar.ir/api/{self.metapost.bot.bot_token}/sendMessage'
        try:
            response = requests.post(url=url, data=data)
            response_message = response.text
            message_id = json.loads(response_message)['result']['message_id']
        except Exception as e:
            message_id = 0
            response_message = str(e)
        self.metapost.message_id = message_id
        self.metapost.save()
        EitaaBotHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                       chat_id=self.chat_id,
                                       message_id=message_id)
        return print(response_message)


def eitaa_send_text_with_file(metapost, chat_id, title, text, file_url):
    EitaaSendTextWithFileThread(metapost=metapost, chat_id=chat_id, title=title, text=text, file_url=file_url).start()


class EitaaSendTextWithFileThread(threading.Thread):
    def __init__(self, metapost, chat_id, title, text, file_url):
        super().__init__()
        self.metapost = metapost
        self.chat_id = chat_id
        self.title = title
        self.text = text
        self.file_url = file_url

    def run(self):
        file_name_path_from_url = str(self.metapost.attached_file_link).split('/')[-1].split('.')
        file_ext = file_name_path_from_url[-1]
        print(file_ext)
        response = requests.get(self.file_url)
        if response.status_code == 200:
            file_content = (ContentFile(response.content))
        else:
            response_message = f"Failed to download image. Status code: {response.status_code}"
            return print(response_message)
        print(f'file_content: {file_content.name}')
        files = {
            'file': (file_ext, file_content)
        }

        data = {
            'chat_id': self.chat_id,
            'title': self.title,
            'caption': self.text,
        }

        url = f'https://eitaayar.ir/api/{self.metapost.bot.bot_token}/sendFile'
        try:
            response = requests.post(url=url, data=data, files=files)
            response_message = response.text
            message_id = json.loads(response_message)['result']['message_id']
        except Exception as e:
            message_id = 0
            response_message = str(e)
        self.metapost.message_id = message_id
        self.metapost.save()
        EitaaBotHistory.objects.create(metapost=self.metapost, response_message=response_message,
                                       chat_id=self.chat_id,
                                       message_id=message_id)
        return print(response_message)


def eitaa_message_handler(metapost):
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
                eitaa_send_simple_text(metapost=metapost, chat_id=channel, title=metapost.title, text=content)
            else:
                eitaa_send_text_with_file(metapost=metapost, chat_id=channel, title=metapost.title,
                                          text=content,
                                          file_url=metapost.attached_file_link)
        elif metapost.action == 'republish':
            if metapost.metapost_view_type == 'simple_text':
                eitaa_send_simple_text(metapost=metapost, chat_id=channel, title=metapost.title, text=content)
            else:
                eitaa_send_text_with_file(metapost=metapost, chat_id=channel, title=metapost.title,
                                          text=content,
                                          file_url=metapost.attached_file_link)
        elif metapost.action == 'revise':
            pass
        elif metapost.action == 'delete':
            pass
