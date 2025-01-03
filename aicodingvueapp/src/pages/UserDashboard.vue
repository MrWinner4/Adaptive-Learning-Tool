<template>
    <h1>Dashboard</h1>
    <div class = "lessons">
            <div v-for="lesson in lessons" :key = "lesson.id" class = "lesson-card">
                <h3>{{ lesson.title }}</h3>
                <p>{{  lesson.description }}</p>
                <button @click="viewLesson(lesson.id)">Start Lesson</button>
            </div>
    </div>
</template>

<script>
import axiosInstance from '../axios';
export default {
  name: 'UserDashboard',
  data() {
    return {
      lessons: [],
    };
  },
  methods: {
    async fetchLessons() {
      try {
        const response = await axiosInstance.get('/lessons/lessons/')
        this.lessons = response.data;
      } catch (error) {
        console.error('Error fetching lessons:', error.response || error);
      }
    },
    viewLesson(id) {
        this.$router.push(`/lessons/${id}/lecture`);
    },
  },
  created() {
    this.fetchLessons();
  },
};
</script>




<style>
    .lessons {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        justify-content: center;
    }
    .lesson-card {
        border: 1px solid rgb(118, 146, 255);
        padding: 10px;
        border-radius: 5px;
        width: 200px;
        box-shadow: 2px 2px 5px rgba(32, 32, 32, .2);
        list-style: none;
    }
    button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
        border-radius: 5px;
    }
    button:hover {
          background-color: #0056b3;
    }
</style>