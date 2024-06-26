from rest_framework import authentication, exceptions
import firebase_admin.auth as auth
from django.contrib.auth.models import User

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        id_token = request.headers.get('Authorization')

        if not id_token:
            return None

        if id_token.startswith('Bearer '):
            id_token = id_token[7:]

        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception as e:
            raise exceptions.AuthenticationFailed('Invalid Firebase ID token')

        uid = decoded_token.get('uid')
        email = decoded_token.get('email')

        if not uid or not email:
            raise exceptions.AuthenticationFailed('Invalid Firebase ID token')

        user = User(uid, email)

        return (user, None)
