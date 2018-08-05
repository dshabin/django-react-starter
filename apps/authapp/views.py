from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.http import JsonResponse
from .models import UserProfile
from django.contrib.auth import authenticate, login

# Create your views here.

class SignupView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        email = data.get('email', None)
        password = data.get('password', None)
        try:
            user = User.objects.create_user(username=email,email=email,password=password)
            user_profile , _ = UserProfile.objects.get_or_create(user=user,email=email)
            user = authenticate(username = email, password = password)
            if user is not None:
                token , _ = Token.objects.get_or_create(user=user)
                return JsonResponse({ "token" : str(token) , "email" : email })
        except Exception as e:
            print(e.message)
            return JsonResponse({ "error" : "Bad signup" })

class LoginView(APIView):

    #authentication_classes = (SessionAuthentication,)
    def post(self, request, format=None):
        data = json.loads(request.body)
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username = email, password = password)
        if user is not None:
            token , _ = Token.objects.get_or_create(user=user)
            return JsonResponse({ "token" : str(token) , "email" : email })
        else:
            return JsonResponse({ "error" : "Bad login"})
