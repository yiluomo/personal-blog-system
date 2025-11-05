<template>
  <div class="works-section">
    <div class="container">
      <h2 class="section-title">我的作品</h2>
      <div class="works-grid">
        <div 
          v-for="(work, index) in works" 
          :key="work.id"
          class="work-card"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <div class="work-image">
            <img :src="work.cover_image" :alt="work.title" />
            <div class="work-overlay">
              <a v-if="work.link" :href="work.link" target="_blank" class="view-btn">
                <i class="fas fa-external-link-alt"></i> 查看详情
              </a>
            </div>
          </div>
          <div class="work-content">
            <h3 class="work-title">{{ work.title }}</h3>
            <p class="work-desc">{{ work.desc }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../utils/axios'

const works = ref([])

const loadWorks = async () => {
  try {
    const data = await axios.get('/works/')
    works.value = data.results || data
  } catch (error) {
    console.error('加载作品失败:', error)
  }
}

onMounted(() => {
  loadWorks()
})
</script>

<style scoped>
.works-section {
  min-height: 100vh;
  padding: 4rem 2rem;
  position: relative;
  z-index: 2;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  color: white;
  margin-bottom: 3rem;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.works-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.work-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: all 0.3s;
  animation: slideUp 0.8s ease-out both;
}

.work-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(255, 105, 180, 0.3);
}

.work-image {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.work-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.work-card:hover .work-image img {
  transform: scale(1.1);
}

.work-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 105, 180, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.work-card:hover .work-overlay {
  opacity: 1;
}

.view-btn {
  padding: 0.8rem 1.5rem;
  background: white;
  color: #FF69B4;
  border-radius: 25px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s;
}

.view-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.work-content {
  padding: 1.5rem;
}

.work-title {
  font-size: 1.3rem;
  color: #333;
  margin-bottom: 0.5rem;
}

.work-desc {
  color: #666;
  line-height: 1.6;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .works-grid {
    grid-template-columns: 1fr;
  }
}
</style>
