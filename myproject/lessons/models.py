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
    questions = models.JSONField

    def __str__(self):
        return f"Quiz for {self.lesson.title}"
    
class Interactive(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="interactive")
    prompt = models.TextField()

    def __str__(self):
        return f"Interactive for {self.lesson.title}"
    