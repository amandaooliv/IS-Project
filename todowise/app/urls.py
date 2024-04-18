from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('course/<int:course_id>/', views.course_list, name='course_list'),
    path('student/', views.student_list, name='student_list'),
    path('user/', views.user_list, name='user_list'),
    path('course/<int:course_id>/remove/<int:subject_id>', views.remove_subject, name='remove_subject'),
    path('course/<int:course_id>/done/<int:subject_id>', views.done_subject, name='done_subject'),
    #path('course/<int:course_id>/status/<int:subject_id>', views.status_student, name='status_student'),
    path('subject/<int:course_id>/<int:subject_id>/', views.open_subject, name='open_subject'),
    path('subject/<int:course_id>/<int:subject_id>/add_grade/', views.add_grade, name='add_grade'),
    path('update_grade/<int:grade_id>/', views.update_grade, name='update_grade'),
    path('update_status/<int:student_id>/', views.update_status, name='update_status'),
]

