<template>
  <div>
    <h1>전체 영화 목록 페이지</h1>
    <h3>최고 평점 영화</h3>
    <div v-if="movies.length" class="movie-list">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
    <div v-else>
      <p>영화를 불러오는 중...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import MovieCard from "../components/MovieCard.vue";

const movies = ref([]);

const fetchTopRatedMovies = async () => {
  const apiKey = import.meta.env.VITE_TMDB_API_KEY; // TMDB API 키
  const url = `https://api.themoviedb.org/3/movie/top_rated?api_key=${apiKey}&language=ko-KR&page=1`;

  try {
    const response = await axios.get(url);
    movies.value = response.data.results; // ref로 선언된 movies 업데이트
  } catch (error) {
    console.error("error = ", error);
  }
};

onMounted(() => {
  fetchTopRatedMovies();
});
</script>

<style scoped>
.movie-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
</style>
