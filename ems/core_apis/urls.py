from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    re_path('signup', views.signup, name='signup'),
    re_path('login', views.login, name='login'),

    re_path('token_test', views.token_test, name='test token'),
]