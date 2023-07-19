from django.shortcuts import render

# Create your views here.
'''
DJango Rest Framework
Create API using generic view.
Create login API with 1 Min Session timeout.
(Token should be valid till 1 min)
'''
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from api.create_token import *
from api.serializers import LoginSerializer,UserSerializer
from rest_framework import status

class RegistrationViewSet(CreateModelMixin,GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginAPIView(CreateModelMixin,ListModelMixin,GenericViewSet):
    serializer_class= LoginSerializer
    queryset=User.objects.all()
    
    def create(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            print('token',token)
            if user.is_active:
                dict = {'first_name':user.first_name,'last_name':user.last_name,'token':token,'email':user.email}
                return Response({'status':1,'message':'Logged in successfully','data':dict},status=status.HTTP_200_OK)
            
        return Response({'status':0,'message':'invalid Creds'})

    def list(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        user = get_user_from_token(token)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'status':0,'message':'invalid/Expired Creds'})
   
  