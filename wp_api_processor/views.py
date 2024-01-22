import json

from django.http import JsonResponse
from django.views import View
from utilities.http_metod import fetch_data_from_http_post
from utilities.utilities import create_json, decrypt_text
from custom_logs.models import custom_log


from wp_api_processor.models import WpUsers
from yekjamodir.settings import WP_DATA_DECRYPTING_KEY


class WPAPIProcessorView(View):

    def __init__(self):
        super().__init__()
        self.context = {}

    def get(self, request, *args, **kwargs):
        return create_json('get', request, 'ناموفق', 'درخواست غیر مجاز')

    def post(self, request, *args, **kwargs):
        user_data_encrypted = fetch_data_from_http_post(request, 'xyz', self.context)
        if not user_data_encrypted:
            return create_json('post', request, 'ناموفق', 'درخواست غیر مجاز')
        try:
            encrypted_text = user_data_encrypted
            decryption_password = WP_DATA_DECRYPTING_KEY
            decrypted_text = decrypt_text(encrypted_text, decryption_password)
            custom_log(json.dumps(json.loads(decrypted_text)))
            try:
                front_input = json.loads(decrypted_text)
                try:
                    user_id = front_input['user_id']
                    if user_id == '':
                        user_id = None
                except:
                    user_id = None
                try:
                    user_login = front_input['user_login']
                    if user_login == '':
                        user_login = None
                except:
                    user_login = None
                try:
                    wp_user = WpUsers.objects.get(id=user_id, user_login=user_login)
                    return JsonResponse({'message': f'خوش آمدید کاربر {wp_user.user_login}'})
                except:
                    return create_json('post', request, 'ناموفق', 'کاربر غیر مجاز')

            except:
                return create_json('post', request, 'ناموفق', 'ورودی صحیح نیست')
        except Exception as e:
            custom_log(f'{e}')
            return JsonResponse({'message': f'request failed'})

    def put(self, request, *args, **kwargs):
        return create_json('put', request, 'ناموفق', 'درخواست غیر مجاز')

    def delete(self, request, *args, **kwargs):
        return create_json('delete', request, 'ناموفق', 'درخواست غیر مجاز')


