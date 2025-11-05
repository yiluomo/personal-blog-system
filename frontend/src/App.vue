<template>
  <div class="app-container">
    <CherryBlossomAnimation />
    <router-view />
  </div>
</template>

<script setup>
import CherryBlossomAnimation from './components/CherryBlossomAnimation.vue'
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  position: relative;
  overflow-x: hidden;
}

.app-container::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23FFB7C5" fill-opacity="0.1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,138.7C960,139,1056,117,1152,106.7C1248,96,1344,96,1392,96L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') repeat-x;
  background-size: cover;
  opacity: 0.3;
  animation: breathe 8s ease-in-out infinite;
  pointer-events: none;
  z-index: 0;
}

@keyframes breathe {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.5; }
}
</style>
