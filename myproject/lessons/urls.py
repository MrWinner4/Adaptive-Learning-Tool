from django.urls import path
from .views import lesson_list, lesson_lecture, quiz_detail, submit_quiz
from myproject.lessons.aituils import generate_feedback

urlpatterns = [
    path('lessons/', lesson_list, name='lesson_list'),
    path('<int:id>/lecture/', lesson_lecture, name='lesson_lecture'),
    path('<int:id>/quiz/', quiz_detail, name='quiz_detail'),
    path('<int:id>/submit_quiz/', submit_quiz, name='submit_quiz'),
    path('api/feedback/', generate_feedback, name='generate_feedback'),

]