from functools import partial
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.backends import TokenBackend
from datetime import timedelta
from rest_framework_simplejwt.tokens import UntypedToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    #access_token = refresh.access_token
    #access_token.set_exp(lifetime=timedelta(minutes=1))
    return str(refresh)

def get_user_from_token(token):
    #try:
        valid_data = TokenBackend(algorithm='HS256').decode(str(token),None)
        
        try:
            data = UntypedToken(token)
            user = valid_data
            print(user)
            user_id = user['user_id']
            try:
                user = User.objects.get(pk =user_id )
                return user
            except:
                return 0
        except:
            return 0