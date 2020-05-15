# chat/routing.py
from django.urls import re_path

from . import consumers as chatconsumers
from reportcards import consumers as reportcardsconsumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', chatconsumers.ChatConsumer),
    re_path(r'ws/studentresults/marksbystudent/(?P<mkl>\w+)/(?P<std>\w+)/$', reportcardsconsumers.ScoreConsumer),
    re_path(r'ws/studentresults/marksbysubject/(?P<mkl>\w+)/(?P<std>\w+)/$', reportcardsconsumers.SubjectScoreConsumer),
    re_path(r'ws/studentresults/marklistbystream/(?P<mkl>\w+)/$', reportcardsconsumers.StreamScoreConsumer),
    re_path(r'ws/studentresults/classmarklist/(?P<mkl>\w+)/$', reportcardsconsumers.ClassScoreConsumer),
]