# chat/routing.py
from django.urls import re_path
from . import consumers
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    
]