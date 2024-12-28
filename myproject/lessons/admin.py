from django.contrib import admin
from .models import Lesson, Quiz, Interactive, Question
# Register your models here.

admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Interactive)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'quiz') #Lists them out so I don't have to click on them
    search_fields = ('question_text', 'quiz__lesson__title')  # Searching by question or lesson
    list_filter = ('quiz__lesson__title',)  # Filters the questions
    ordering = ('quiz__lesson__title',)  # Orders by title