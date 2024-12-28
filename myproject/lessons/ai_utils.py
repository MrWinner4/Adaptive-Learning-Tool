import sys
import os
import django

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Replace 'myproject' with your actual project name

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
django.setup()

# Import your model
from lessons.models import Question, Quiz, Lesson  # Use relative import since the script is now in the same app
import google.generativeai as genai
import json

#Supressing warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

genai.configure(api_key=os.getenv("BARD_API_KEY"))
def save_questions_from_json(jsonData, subject):

    try:
        # Print raw JSON data for inspection
        print(f"Raw JSON Response: {jsonData}")

        # Attempt to load the JSON data
        data = json.loads(jsonData)
        data = json.loads(jsonData)
        questions = data["questions"]
        
        lesson = Lesson.objects.get(title=subject)

        quiz, created = Quiz.objects.get_or_create(lesson = lesson)

        for q in questions:
            Question.objects.create(
                quiz = quiz,
                question_text = q["question"],
                option_a=q["options"]["A"],
                option_b=q["options"]["B"],
                option_c=q["options"]["C"],
                option_d=q["options"]["D"],
                correct_answer=q["answer"],
                explanation=q["explanation"],
            )
        print(f"Successful! {subject}")
    except Lesson.DoesNotExist:
        print(f"Lesson with title '{subject}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")
    
def GenerateQuestion(topic, num_questions = 20):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config = {"response_mime_type": "application/json"}
        )
    response = model.generate_content(
        f"""
        Create {num_questions} multiple-choice question about "{topic}".
        Include a variety of easy, medium, and hard choices. Keep in mind that
        these will be for highschool students currently learning the concepts.
        Seperate each question "block" by 2 new lines.
        Include:
        1. The question text.
        2. Four options (A, B, C, D).
        3. Indicate the correct answer and provide a short explanation.
        """
    )
    save_questions_from_json(response.text, topic)

#if __name__ == "__main__":
    #Put GenerateQuestion("subject") for what you want generated here
    #Possibility of generating new questions each week or something?
    #Free too!