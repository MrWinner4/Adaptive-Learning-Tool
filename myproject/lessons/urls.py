from django.urls import path
from .views import lesson_list, lesson_lecture

urlpatterns = [
    path('lessons/', lesson_list, name='lesson_list'),
    path('<int:id>/lecture/', lesson_lecture, name='lesson_lecture'),

]