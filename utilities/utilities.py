import jdatetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import hashlib

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def create_json(method, request, result, message):
    body = {
        'method': method,
        'request': request,
        'result': result,
        'message': message
    }
    return body


def date_string_to_date_format(date_in_string):
    try:
        date_list = str(date_in_string).replace('/', ' ').replace(':', ' ').split()
        date_shamsi = jdatetime.datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]),
                                         hour=int(date_list[3]), minute=int(date_list[4]))
        return date_shamsi
    except Exception as e:
        print(str(e))
        return None


def decrypt_text(encrypted_text, decryption_password):
    # Decode the base64-encoded encrypted text
    encrypted_text_bytes = base64.b64decode(encrypted_text)

    # Extract the initialization vector and encrypted data
    iv_length = 16  # Assuming AES-256-CBC
    iv = encrypted_text_bytes[:iv_length]
    encrypted_data = encrypted_text_bytes[iv_length:]

    # Derive the key from the decryption password using SHA-256
    key = hashlib.sha256(decryption_password.encode()).digest()

    # Decrypt the data using AES-256-CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    return decrypted_data.decode('utf-8')