# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),  # ⭐ 确保有 name='question_list'
    path('add/', views.add_question, name='add_question'),
]