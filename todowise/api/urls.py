from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:course_id>/', views.DetailToDos.as_view())
]