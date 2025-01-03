import { createRouter, createWebHistory } from "vue-router";
import UserDashboard from "../pages/UserDashboard.vue";
import Settings from "../pages/UserSettings.vue";
import LessonLecture from "../pages/LessonLecture.vue";
import LessonQuiz from "../pages/LessonQuiz.vue"

const routes = [
  { path: "/dashboard", name: 'UserDashboard', component: UserDashboard },
  { path: "/settings", component: Settings },
  { path: '/lessons/:id/lecture', name: 'LessonLecture', component: LessonLecture, props: true,},
  { path: '/lessons/:id/quiz', component: LessonQuiz, name: 'LessonQuiz' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
