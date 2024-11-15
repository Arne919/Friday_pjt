<template>
  <div>
    <h1>영화 리뷰 검색</h1>
    <input v-model="query" @keypress.enter="fetchYouTubeVideos" placeholder="영화 제목 입력" />
    <button @click="fetchYouTubeVideos">검색</button>

    <div v-if="videos.length" class="video-list">
      <YouTubeCard
        v-for="video in videos"
        :key="video.id.videoId"
        :videoTitle="video.snippet.title"
        :channelTitle="video.snippet.channelTitle"
        :thumbnail="video.snippet.thumbnails.high.url"
        :videoId="video.id.videoId"
        @open="openModal"
      />
    </div>
    <p v-else-if="query.length && !loading">검색 결과가 없습니다.</p>
    <p v-else>검색어를 입력하세요.</p>

    <YoutubeReviewModal
      :show="showModal"
      :videoId="selectedVideoId"
      @close="closeModal"
    />
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import YouTubeCard from "../components/YouTubeCard.vue";
import YoutubeReviewModal from "../components/YoutubeReviewModal.vue";

export default {
  name: "ReviewSearchView",
  components: {
    YouTubeCard,
    YoutubeReviewModal,
  },
  setup() {
    const query = ref("");
    const videos = ref([]);
    const loading = ref(false);
    const showModal = ref(false);
    const selectedVideoId = ref("");

    const fetchYouTubeVideos = async () => {
      if (!query.value.trim()) return;

      loading.value = true;
      const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY; // YouTube API 키
      const searchQuery = `${query.value} movie review`;
      const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${encodeURIComponent(
        searchQuery
      )}&key=${youtubeApiKey}`;

      try {
        const response = await axios.get(url);
        videos.value = response.data.items;
      } catch (error) {
        console.error("YouTube API 요청 중 오류 발생:", error);
      } finally {
        loading.value = false;
      }
    };

    const openModal = (videoId) => {
      selectedVideoId.value = videoId;
      showModal.value = true;
    };

    const closeModal = () => {
      showModal.value = false;
    };

    return {
      query,
      videos,
      loading,
      showModal,
      selectedVideoId,
      fetchYouTubeVideos,
      openModal,
      closeModal,
    };
  },
};
</script>

<style scoped>
.video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
input {
  padding: 8px;
  font-size: 1em;
  margin-right: 10px;
}
button {
  padding: 8px 12px;
  font-size: 1em;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #369b73;
}
</style>
