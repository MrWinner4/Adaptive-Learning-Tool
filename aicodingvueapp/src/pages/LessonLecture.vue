<template>
    <div class="lecture">
        <h1>{{ lecture.title }}</h1>
        <div v-html="lecture.content"></div>
        <button @click = "viewQuiz(lecture.id)">Take Quiz</button>
    </div>
</template>

<script>
import axiosInstance from '../axios';

export default {
  name: 'LessonLecture',
  data() {
    return {
      lecture: {},
    };
  },
  methods: {
    viewQuiz(id){
        this.$router.push(`/lessons/${id}/quiz`);
        },
    },
    async created() {
    const lessonId = this.$route.params.id;
    try {
      const response = await axiosInstance.get(`/lessons/${lessonId}/lecture/`);
      this.lecture = response.data; // Setting "lecture" to the response data
    } catch (error) {
      console.error("Error loading lecture: ", error);
    }
  },
};
</script>

<style>

.lecture {
    max-width: 600px;
    margin: 0 auto;
    padding: 0 20px;
    text-align: left;
}
</style>