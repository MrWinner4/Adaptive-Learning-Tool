from django.db import models
from ckeditor.fields import RichTextField

class Lesson(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(default="example description")
    lecture = RichTextField(default="example lecture")
    order = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title
    
class Quiz(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="quiz")

    def __str__(self):
        return f"Quiz for {self.lesson.title}"
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField(default = "example question")
    option_a = models.CharField(max_length = 250)
    option_b = models.CharField(max_length = 250)
    option_c = models.CharField(max_length = 250)
    option_d = models.CharField(max_length = 250)
    correct_answer = models.CharField(max_length = 1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    explanation = models.TextField(default = "explanation")
    
class Interactive(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="interactive")
    prompt = models.TextField()

    def __str__(self):
        return f"Interactive for {self.lesson.title}"
    