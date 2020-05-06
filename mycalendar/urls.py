
from django.urls import path
from . import views

urlpatterns = [
    path('', views.year, name='year'),
    path('month/', views.month, name='month'),
    path('week/', views.week, name='week'),
    path('day/', views.day, name='day'),
    path('period', views.period, name='period'),
]