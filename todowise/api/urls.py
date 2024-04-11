from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.ListToDos.as_view()),
    path('lists/<int:list_id>/', views.DetailToDos.as_view())
]