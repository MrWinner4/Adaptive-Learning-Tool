from django.contrib import admin
from .models import Lesson, Quiz, Interactive
# Register your models here.

admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Interactive)