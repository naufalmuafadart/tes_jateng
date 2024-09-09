import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()


def generate_token(id, phone_number, is_access_token):
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    payload = {
        'id': id,
        'phone_number': phone_number,
        'iat': now,
        'exp': now + datetime.timedelta(hours=3),
    }

    # Define your secret key
    secret_key = os.getenv('ACCESS_TOKEN_SECRET')

    if not is_access_token:
        secret_key = os.getenv('REFRESH_TOKEN_SECRET')

    # Create the token
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def verify_token(token, is_access_token):
    # Define your secret key
    secret_key = os.getenv('ACCESS_TOKEN_SECRET')

    if not is_access_token:
        secret_key = os.getenv('REFRESH_TOKEN_SECRET')

    try:
        # Decode the token
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise Exception("Expired token")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
