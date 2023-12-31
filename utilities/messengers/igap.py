import json
import requests
from social.messengers.igap_proto_buffer.python import ChannelSendMessage_pb2


def send_text_message_to_channels(bot_token, room_id, user_message):
    url = f'https://api.igap.net/botland/v1/api?actionId=201'
    headers = {
        'Authorization': f'Bearer {bot_token}'
    }

    # Create a ChatSendMessage message
    message = ChannelSendMessage_pb2.ChannelSendMessage()
    message.message = f'{user_message}'
    message.room_id = f"@dssdf"

    # Serialize the message to binary
    data = message.SerializeToString()

    response = requests.post(url, data=data, headers=headers)
    print(response)
    # Check the response
    if response.status_code == 200:
        print('Request successful')
    else:
        print(f'Request failed with status code {response.status_code}')







    url = 'https://api.igap.net/botland/v1/api?actionId=201'

    headers = {"Authorization": f"Bearer {bot_token}"}
    data = {
        "message": f"{message}",
        "message_type": "TEXT",
        "room_id": f"{room_id}",
    }
    r = requests.post(url, headers=headers, data=data)
    return r.text
