
from django.urls import path
from . import views

urlpatterns = [
    path('', views.creat_marklist, name='creat_marklist'),
    path('<mkl>', views.setup_marklist, name='setup_marklist'),
    path('marklist/<pk>/', views.marklist, name='marklist'),

    path('marksbysubject/<mkl>/<sub>/', views.marks_by_subject, name='marks_by_subject'),
    path('marksbystudent/<mkl>/<std>/', views.marks_by_student, name='marks_by_student'),
    path('marklistbystream/<mkl>/', views.marks_by_stream, name='marks_by_stream'),
    path('classmarklist/<klass>/<term>/', views.class_marklist, name='class_marklist'),
]
