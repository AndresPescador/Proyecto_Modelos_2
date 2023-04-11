# todo/todo/urls.py : Main urls.py
from django.urls import include, re_path
from django.urls import path, include
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]