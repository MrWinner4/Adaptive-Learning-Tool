from django.shortcuts import render, get_object_or_404
from .models import Lesson, Quiz, Interactive
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lesson, Question
from .serializers import QuizSerializer
from django.http import JsonResponse
from .aiutils import generate_feedback
import random


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
            'content': lesson.lecture,  # Return the lecture content
            'id': id,
        })
    except Lesson.DoesNotExist:
        return JsonResponse({'error': 'Lesson not found'}, status=404)
    
@api_view(['GET'])
def quiz_detail(request, id):
    quiz = get_object_or_404(Quiz, lesson_id = id)
    questions = list(quiz.questions.all())
    random.shuffle(questions)
    selected_questions = questions[:5]
    serializer = QuizSerializer({'lesson': quiz.lesson, 'questions': selected_questions})
    return Response(serializer.data)

@api_view(['POST'])
def submit_quiz(request, id):
    quiz = get_object_or_404(Quiz, lesson_id=id)
    
    answers = request.data.get('answers', {})
    
    correct_answers = 0
    incorrect_answers = []

    for question_id, user_answer in answers.items():
        question = get_object_or_404(Question, id=question_id, quiz=quiz)
        
        if question.correct_answer == user_answer:
            correct_answers += 1
        else:
            incorrect_answers.append({
                "id": question.id,
                "question_text": question.question_text,
                "user_answer": user_answer,
                'lesson_title': question.quiz.lesson.title,
                "correct_answer": question.correct_answer,
            })

    total_questions = 5

    return Response({
        "correct_answers": correct_answers,
        "incorrect_answers": incorrect_answers,
        "total_questions": total_questions,
    })

api_view(['POST'])
def get_feedback(request):
    subject = request.data.get('subject')
    question = request.data.get('question')
    all_answers = request.data.get('all_answers')
    incorrect_answer = request.data.get('incorrect_answer')

    if not (subject and question and all_answers and incorrect_answer):
        return Response({"error": "Missing paramenters"}, status=400)
    try:
        feedback = generate_feedback(subject, question, incorrect_answer)
        return Response({"feedback": feedback})
    except Exception as e:
        return Response({"error": str(e)}, status=500)