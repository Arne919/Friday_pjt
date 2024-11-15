<template>
  <div class="movie-card">
    <RouterLink :to="`/movies/${movie.id}`">
      <img :src="imageUrl" alt="movie poster" />
      <h2>{{ movie.title }}</h2>
      <p>평점: {{ movie.vote_average }}</p>
    </RouterLink>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  computed: {
    imageUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`;
    },
  },
};
</script>

<style scoped>
.movie-card {
  border: 1px solid #ddd;
  padding: 16px;
  margin: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 300px;
  text-align: center;
}
.movie-card img {
  width: 100%;
  height: auto;
  border-radius: 4px;
}
</style>
