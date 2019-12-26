from google.oauth2 import id_token
from google.auth.transport import requests
from puntLilaAPI.config import id


def is_valid_user(token: str) -> int or None:
    try:
        # Specify the CLIENT_ID of the app that accesses the backend
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), id)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        # ID token is valid. Return the user's Google Account ID from the decoded token.
        return idinfo['sub']
    except ValueError:
        # Invalid token
        return None


def user_is_admin(id: int) -> bool:
    # TODO check if id is admin in firebase
    return True
