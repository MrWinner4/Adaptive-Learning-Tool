from django.urls import path
from .views import lesson_list, lesson_lecture, quiz_detail, submit_quiz

urlpatterns = [
    path('lessons/', lesson_list, name='lesson_list'),
    path('<int:id>/lecture/', lesson_lecture, name='lesson_lecture'),
    path('<int:id>/quiz/', quiz_detail, name='quiz_detail'),
    path('lessons/<int:id>/submit_quiz/', submit_quiz, name='submit_quiz'),

]