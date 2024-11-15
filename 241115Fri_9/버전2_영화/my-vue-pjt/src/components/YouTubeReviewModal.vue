<template>
  <div v-if="show" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <iframe
        v-if="videoId"
        :src="`https://www.youtube.com/embed/${videoId}`"
        frameborder="0"
        allowfullscreen
      ></iframe>
      <p v-else>동영상을 불러올 수 없습니다.</p>
      <button @click="closeModal" class="close-button">닫기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "YoutubeReviewModal",
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
  text-align: center;
}

iframe {
  width: 100%;
  height: 400px;
}

.close-button {
  margin-top: 10px;
  padding: 8px 16px;
  background: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.close-button:hover {
  background: #d32f2f;
}
</style>
