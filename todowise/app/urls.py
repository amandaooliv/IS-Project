from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('course/<int:course_id>/', views.course_list, name='course_list'),
    #path('course/<int:course_id>/add/', views.add_subject, name='add_subject'),
    path('student/', views.student_list, name='student_list'),
    #path('student/<int:student_id>/', views.student_list, name='student_list'),
    #path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    #path('register/<int:register_id>/add/', views.add_subject, name='add_subject'),
    path('course/<int:course_id>/remove/<int:subject_id>', views.remove_subject, name='remove_subject'),
    path('course/<int:course_id>/done/<int:subject_id>', views.done_subject, name='done_subject'),
    path('subject/<int:course_id>/<int:subject_id>/', views.open_subject, name='open_subject'),
]

