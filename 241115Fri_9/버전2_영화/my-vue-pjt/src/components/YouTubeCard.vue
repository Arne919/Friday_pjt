<template>
  <div class="youtube-card" @click="openVideo">
    <img :src="thumbnail" alt="thumbnail" />
    <h3>{{ videoTitle }}</h3>
    <p>{{ channelTitle }}</p>
  </div>
</template>

<script>
export default {
  name: "YouTubeCard",
  props: {
    videoTitle: {
      type: String,
      required: true,
    },
    channelTitle: {
      type: String,
      required: true,
    },
    thumbnail: {
      type: String,
      required: true,
    },
    videoId: {
      type: String,
      required: true,
    },
  },
  methods: {
    openVideo() {
      this.$emit("open", this.videoId);
    },
  },
};
</script>

<style scoped>
.youtube-card {
  border: 1px solid #ddd;
  padding: 16px;
  margin: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 300px;
  text-align: center;
  cursor: pointer;
}
.youtube-card img {
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin-bottom: 10px;
}
.youtube-card h3 {
  font-size: 1.1em;
  margin: 10px 0;
}
</style>
