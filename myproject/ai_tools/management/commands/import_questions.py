import json
from django.core.management.base import BaseCommand, CommandParser
from lessons.models import Lesson
from myproject.lessons.ai_utils import save_questions_from_json

class Command(BaseCommand):
    help = "Import questions from a json file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the JSON file")
        parser.add_argument('lesson_id', type=int, help="Lesson's ID")
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        lesson_id = kwargs['lesson_id']

        try:
            lesson = Lesson.objects.get(id = lesson_id)
            with open(file_path, 'r') as file:
                jsonData = file.read()
                save_questions_from_json(jsonData, lesson)
                self.stdout.write(self.style.SUCCESS("Succesful Import."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
