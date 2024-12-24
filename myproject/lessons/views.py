from django.shortcuts import render, get_object_or_404
from .models import Lesson, Quiz, Interactive

def lessonList(request):
    lessons = Lesson.objects.order_by('order')
    return render(request, 'lesson_list.html', {'lessons': lessons})

def lessonText(request, lesson_id):
    lesson = get_object_or_404(Lesson, lesson_id)
    return render(request, 'lesson_text.html', {'lesson': lesson})

def lessonQuiz(request, lesson_id):
    quiz = get_object_or_404(Quiz, lesson_id)
    return render(request, 'lesson_quiz.html', {'quiz': quiz})

def lessonInteractive(request, lesson_id):
    interactive = get_object_or_404(Interactive, lesson_id)
    return render(request, 'lesson_interactive', {'interactive': interactive}),