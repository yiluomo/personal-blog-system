<template>
  <div class="carousel-container">
    <div class="carousel-wrapper">
      <div 
        v-for="(item, index) in images" 
        :key="item.id"
        class="carousel-item"
        :class="{ active: currentIndex === index }"
      >
        <img :src="item.image" :alt="`轮播图 ${index + 1}`" />
      </div>
    </div>
    
    <div class="carousel-controls">
      <button @click="prev" class="control-btn">
        <i class="fas fa-chevron-left"></i>
      </button>
      <button @click="next" class="control-btn">
        <i class="fas fa-chevron-right"></i>
      </button>
    </div>
    
    <div class="carousel-indicators">
      <span 
        v-for="(item, index) in images" 
        :key="index"
        class="indicator"
        :class="{ active: currentIndex === index }"
        @click="goTo(index)"
      ></span>
    </div>
    
    <div class="scroll-hint" @click="scrollDown">
      <i class="fas fa-chevron-down"></i>
      <p>向下滚动</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from '../utils/axios'

const images = ref([])
const currentIndex = ref(0)
let autoPlayTimer = null

const loadImages = async () => {
  try {
    const data = await axios.get('/carousel/')
    images.value = data.results || data
  } catch (error) {
    console.error('加载轮播图失败:', error)
  }
}

const next = () => {
  currentIndex.value = (currentIndex.value + 1) % images.value.length
}

const prev = () => {
  currentIndex.value = (currentIndex.value - 1 + images.value.length) % images.value.length
}

const goTo = (index) => {
  currentIndex.value = index
}

const scrollDown = () => {
  window.scrollTo({
    top: window.innerHeight,
    behavior: 'smooth'
  })
}

const startAutoPlay = () => {
  autoPlayTimer = setInterval(next, 5000)
}

const stopAutoPlay = () => {
  if (autoPlayTimer) {
    clearInterval(autoPlayTimer)
  }
}

onMounted(() => {
  loadImages()
  startAutoPlay()
})

onUnmounted(() => {
  stopAutoPlay()
})
</script>

<style scoped>
.carousel-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.carousel-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

.carousel-item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.carousel-item.active {
  opacity: 1;
  z-index: 1;
}

.carousel-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-controls {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  display: flex;
  justify-content: space-between;
  padding: 0 2rem;
  z-index: 2;
}

.control-btn {
  background: rgba(255, 255, 255, 0.3);
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  transition: all 0.3s;
  backdrop-filter: blur(10px);
}

.control-btn:hover {
  background: rgba(255, 183, 197, 0.6);
  transform: scale(1.1);
}

.carousel-indicators {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 1rem;
  z-index: 2;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 0.3s;
}

.indicator.active {
  background: #FFB7C5;
  transform: scale(1.3);
}

.scroll-hint {
  position: absolute;
  bottom: 4rem;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  color: white;
  cursor: pointer;
  animation: bounce 2s infinite;
  z-index: 2;
}

.scroll-hint i {
  font-size: 2rem;
  display: block;
  margin-bottom: 0.5rem;
}

.scroll-hint p {
  font-size: 0.9rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

@keyframes bounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(-10px); }
}

@media (max-width: 768px) {
  .carousel-controls {
    padding: 0 1rem;
  }
  
  .control-btn {
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
}
</style>
