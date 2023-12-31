import json
import os

import requests


def send_text_message_to_channels(bot_token, channel_id, message):
    url = 'https://api.gap.im/sendMessage'
    headers = {"token": f"a07b5160706a7eb7670b36ccf559e71e696bd21f88a520d64d81406a51994b65"}
    data = {
        "chat_id": f"@callback_bot",
        # "chat_id": f"989125502517",
        "type": "text",
        "data": f"{message}",
        "reply_keyboard": "",
        "inline_keyboard": "",
        "form": ""
    }
    r = requests.post(url, headers=headers, data=data)
    return r.text


def send_text_message_to_user(bot_token, user_id_or_phone_number, message):
    url = 'https://api.gap.im/sendMessage'
    headers = {"Authorization": f"token {bot_token}"}
    data = {
        # "chat_id": f"{user_id_or_phone_number}",
        # "type": "text",
        # "data": f"{message}",
        # "reply_keyboard": "",
        # "inline_keyboard": "",
        # "form": ""
    }
    r = requests.post(url, headers=headers, json=data)
    return r.text


def send_image_to_user(bot_token, chat_id, json_response_of_uploaded_file):
    url = 'https://api.gap.im/sendMessage'
    headers = {"token": f"{bot_token}"}
    data = {
        "chat_id": f"{chat_id}",
        "type": "image",
        "data": json.dumps(json_response_of_uploaded_file),
        # "reply_keyboard": "",
        # "inline_keyboard": "",
        # "form": ""
    }
    r = requests.post(url, headers=headers, data=data)
    return json.loads(r.content)


def gap_upload_file(bot_token, chat_id, file, desc):
    url = 'https://api.gap.im/upload'
    headers = {"token": f"{bot_token}"}
    files = {
        'file': open(file.path, 'rb')
    }
    data = {
        "chat_id": f"{chat_id}",
        "desc": f"{desc}"
    }
    r = requests.post(url, headers=headers, data=data, files=files)
    return json.loads(r.content)
