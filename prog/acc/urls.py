from django.contrib import admin
from django.urls import path, include
from .views import hello

app_name = "account"
urlpatterns = [
    path("hello/", hello, name='hello')
]
