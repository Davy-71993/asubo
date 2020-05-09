
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gaming, name='gaming'),
    path('draft/', views.game, name='draft'),
]
