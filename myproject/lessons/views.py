from django.shortcuts import render, get_object_or_404
from .models import Lesson, Quiz, Interactive
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lesson
from .serializers import LessonSerializer
from django.http import JsonResponse


def lessonList(request):
    lessons = Lesson.objects.order_by('order')
    return render(request, 'lesson_list.html', {'lessons': lessons})

def lessonText(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return JsonResponse({
        'title': Lesson.title,
        'lecture': Lesson.lecture
    })

def lessonQuiz(request, lesson_id):
    quiz = get_object_or_404(Quiz, lesson_id)
    return render(request, 'lesson_quiz.html', {'quiz': quiz})

def lessonInteractive(request, lesson_id):
    interactive = get_object_or_404(Interactive, lesson_id)
    return render(request, 'lesson_interactive', {'interactive': interactive}),

@api_view(['GET'])
def lesson_list(request):
    lessons = Lesson.objects.values('id', 'title', 'description')
    return JsonResponse(list(lessons), safe = False)


@api_view(['GET'])
def lesson_lecture(request, id):
    try:
        lesson = Lesson.objects.get(id=id)
        return Response({
            'title': lesson.title,  # Return the title of the lesson
            'content': lesson.lecture  # Return the lecture content
        })
    except Lesson.DoesNotExist:
        return JsonResponse({'error': 'Lesson not found'}, status=404)