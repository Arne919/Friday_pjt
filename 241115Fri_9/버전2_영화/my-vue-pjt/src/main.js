import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
// const tmdbApiKey = import.meta.env.VITE_TMDB_API_KEY;
// const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY;

app.use(createPinia())
app.use(router)

app.mount('#app')
