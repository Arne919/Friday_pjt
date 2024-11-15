<template>
  <div v-if="show" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <iframe
        v-if="videoId"
        :src="`https://www.youtube.com/embed/${videoId}`"
        frameborder="0"
        allowfullscreen
      ></iframe>
      <p v-else>영화 예고편을 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "YouTubeTrailerModal",
  props: {
    show: {
      type: Boolean,
      required: true,
    },
    videoId: {
      type: String,
      required: false,
      default: "",
    },
  },
  methods: {
    closeModal() {
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 800px;
  width: 90%;
}

iframe {
  width: 100%;
  height: 400px;
}
</style>
