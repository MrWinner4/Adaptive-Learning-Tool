from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_list, name = 'lesson_list'),
    path('<int:lesson_id>/', views.lesson_text, name = 'lesson_text'),
    path('<int:lesson_id>/quiz', views.lesson_quiz, name = 'lesson_quiz'),
    path('<int:lesson_id>/interactive', views.lesson_interactive, name = 'lesson_interactive'),
]
