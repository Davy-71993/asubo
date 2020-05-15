
from django.urls import path
from . import views

urlpatterns = [
    path('year', views.year, name='year'),
    path('', views.month, name='calendar'),
    path('week/', views.week, name='week'),
    path('day/', views.day, name='day'),
    path('period', views.period, name='period'),
]