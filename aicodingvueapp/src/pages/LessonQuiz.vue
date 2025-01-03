<template>
    <div class="quiz" v-if="quiz">
      <h1>{{ quiz.lesson.title }} Quiz</h1>
      <form @submit.prevent="submitQuiz">
      <div v-for="question in quiz.questions" :key="question.id" class="question">
        <h3>{{ question.question_text }}</h3>
        <ul>
            <li class = "answer">
                <label>
                <input type="radio" :name="question.id" value="A" />
                {{ question.option_a }}
                </label>
            </li>
            <li class = "answer">
                <label>
                <input type="radio" :name="question.id" value="B" />
                {{ question.option_b }}
                </label>
            </li>
            <li class = "answer">
                <label>
                <input type="radio" :name="question.id" value="C" />
                {{ question.option_c }}
                </label>
            </li>
            <li class = "answer">
                <label>
                <input type="radio" :name="question.id" value="D" />
                {{ question.option_d }}
                </label>
            </li>
        </ul>
      </div>

      <button type="submit">Submit Quiz</button>
    </form>
    </div>
    <div v-else>
      <p>Loading quiz...</p>
    </div>
  </template>
  
  <script>
  import axiosInstance from '../axios';
  export default {
    name: 'LessonQuiz',
    data() {
      return {
        quiz: null,
        answers: {},
      };
    },
    async created() {
      const lessonId = this.$route.params.id;
      try {
        const response = await axiosInstance.get(`/lessons/${lessonId}/quiz/`);
        this.quiz = response.data;
      } catch (error) {
        console.error('Error fetching quiz:', error.response || error);
      }
    },
    methods: {
    async submitQuiz(event) {
      event.preventDefault();
      try {
        const response = await axiosInstance.post(`/lessons/${this.$route.params.id}/submit_quiz/`, {
            answers: this.answers,
        });
        const { correct_answers, incorrect_answers, total_questions } = response.data;
        console.log(incorrect_answers);
        alert(`You got ${correct_answers} out of ${total_questions} correct!`);
      } catch (error) {
        console.error('Error submitting quiz:', error.response || error);
      }
    },
  },
  };
  </script>
  
  <style>
  .quiz {
    padding: 20px;
  }
  .question {
    margin-bottom: 20px;
    padding: 0 300px;
    }
    ul {
    list-style-type: none;
    padding: 0;
    }
.answer {
      background-color: transparent;
      margin: 15px 0;
      padding: px;
      border: 1px transparent;
      border-radius: 4px;
    }
  </style>
  