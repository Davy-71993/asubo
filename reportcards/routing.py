# chat/routing.py
from django.urls import re_path
from . import consumers
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/reportcards/marksbystudent/(?P<mkl>\w+)/(?P<std>\w+)/$', consumers.ScoreConsumer),
    re_path(r'ws/reportcards/marksbysubject/(?P<mkl>\w+)/(?P<std>\w+)/$', consumers.SubjectScoreConsumer),
    re_path(r'ws/reportcards/marklistbystream/(?P<mkl>\w+)/$', consumers.StreamScoreConsumer),
    re_path(r'ws/reportcards/classmarklist/(?P<mkl>\w+)/$', consumers.ClassScoreConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
]