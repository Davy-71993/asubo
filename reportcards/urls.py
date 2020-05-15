
from django.urls import path
from . import views

urlpatterns = [
    ### Marklists urls
    path('', views.creat_marklist, name='creat_marklist'),
    path('set/<mkl>/', views.setup_marklist, name='setup_marklist'),
    path('marklist/<pk>/', views.marklist, name='marklist'),

    path('marksbysubject/<mkl>/<sub>/', views.marks_by_subject, name='marks_by_subject'),
    path('marksbystudent/<mkl>/<std>/', views.marks_by_student, name='marks_by_student'),
    path('marklistbystream/<mkl>/', views.marks_by_stream, name='marks_by_stream'),
    path('classmarklist/<klass>/<term>/', views.class_marklist, name='class_marklist'),

    ### students urls
    path('students/', views.students, name='students' ),
    path('students/register/', views.add, name='register_student'),
    path('students/import/', views.import_students, name='import_students'),
    path('students/details/<pk>/', views.student, name='student'),
    path('students/delete/<pk>/', views.delete_student, name='delete_student'),

    path('students/house/<hs>/', views.view_by_house, name='students_by_house'),
    path('students/<cl>/', views.view_by_class, name='students_by_class'),
    path('students/<cl>/<strm>/', views.view_by_stream, name='students_by_stream'),

    ### Subjects and Papers
    path('subjects/', views.subjects, name='subjects'),
    path('updatesubject/<pk>/', views.update_subject, name='update_subject'),
    path('deletesubject/<pk>/', views.delete_subject, name='delete_subject'),

    path('addpaper/<pk>/<px>', views.add_paper, name='add_paper'),
    path('editpaper/<pk>/', views.edit_paper, name='edit_paper'),
    path('deletepaper/<pk>/', views.delete_paper, name='delete_paper'),
]
