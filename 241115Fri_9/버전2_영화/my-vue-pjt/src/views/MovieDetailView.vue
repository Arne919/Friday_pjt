<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="imageUrl" alt="movie poster" />
    <p><strong>평점:</strong> {{ movie.vote_average }}</p>
    <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
    <p>{{ movie.overview }}</p>
    <button @click="fetchTrailer">예고편 보기</button>

    <YouTubeTrailerModal
      :show="showModal"
      :videoId="trailerVideoId"
      @close="showModal = false"
    />
  </div>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";
import YouTubeTrailerModal from "../components/YouTubeTrailerModal.vue";

export default {
  name: "MovieDetailView",
  props: {
    movieId: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const movie = ref({});
    const imageUrl = ref("");
    const showModal = ref(false);
    const trailerVideoId = ref("");

    const fetchMovieDetail = async () => {
      const apiKey = import.meta.env.VITE_TMDB_API_KEY; // TMDB API 키
      const url = `https://api.themoviedb.org/3/movie/${props.movieId}?api_key=${apiKey}&language=ko-KR`;

      try {
        const response = await axios.get(url);
        movie.value = response.data;
        imageUrl.value = `https://image.tmdb.org/t/p/w500/${response.data.poster_path}`;
      } catch (error) {
        console.error("Error fetching movie details:", error);
      }
    };

    const fetchTrailer = async () => {
      const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY; // YouTube API 키
      const query = `${movie.value.title} trailer`;
      const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${encodeURIComponent(
        query
      )}&key=${youtubeApiKey}`;

      try {
        const response = await axios.get(url);
        const video = response.data.items[0];
        trailerVideoId.value = video.id.videoId;
        showModal.value = true;
      } catch (error) {
        console.error("Error fetching YouTube trailer:", error);
        showModal.value = true; // 비디오 ID가 없더라도 모달을 띄움
      }
    };

    onMounted(fetchMovieDetail);

    return {
      movie,
      imageUrl,
      showModal,
      trailerVideoId,
      fetchTrailer,
    };
  },
};
</script>

<style scoped>
img {
  max-width: 300px;
  border-radius: 8px;
  margin-bottom: 16px;
}
</style>
