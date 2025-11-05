<template>
  <div class="anime-section">
    <div class="container">
      <div class="section-header">
        <i class="fas fa-film"></i>
        <h2 class="section-title">动漫收藏</h2>
      </div>
      
      <div class="anime-grid">
        <div 
          v-for="anime in animeList" 
          :key="anime.id"
          class="anime-card"
          @click="openAnimeDetail(anime)"
        >
          <div class="anime-cover">
            <img :src="anime.cover" :alt="anime.name" />
            <div class="anime-overlay">
              <div class="anime-rating">
                <i v-for="n in 5" :key="n" class="fas fa-star" :class="{ active: n <= anime.rating }"></i>
              </div>
              <div class="anime-year">{{ anime.year }}</div>
            </div>
          </div>
          <div class="anime-info">
            <h3 class="anime-name">{{ anime.name }}</h3>
            <p class="anime-status" v-if="anime.status">{{ anime.status }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 动漫详情弹窗 -->
    <div v-if="selectedAnime" class="anime-modal" @click="closeAnimeDetail">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="closeAnimeDetail">
          <i class="fas fa-times"></i>
        </button>
        
        <div class="modal-header">
          <img :src="selectedAnime.cover" :alt="selectedAnime.name" class="modal-cover" />
          <div class="modal-info">
            <h2>{{ selectedAnime.name }}</h2>
            <div class="modal-meta">
              <span class="meta-item">
                <i class="fas fa-calendar"></i> {{ selectedAnime.year }}
              </span>
              <span class="meta-item" v-if="selectedAnime.status">
                <i class="fas fa-info-circle"></i> {{ selectedAnime.status }}
              </span>
            </div>
            <div class="modal-rating">
              <i v-for="n in 5" :key="n" class="fas fa-star" :class="{ active: n <= selectedAnime.rating }"></i>
              <span class="rating-text">{{ selectedAnime.rating }}.0</span>
            </div>
            <p class="modal-desc">{{ selectedAnime.desc }}</p>
          </div>
        </div>
        
        <div v-if="selectedAnime.screenshots && selectedAnime.screenshots.length" class="screenshots-section">
          <h3>精彩截图</h3>
          <div class="screenshots-grid">
            <div 
              v-for="screenshot in selectedAnime.screenshots" 
              :key="screenshot.id"
              class="screenshot-item"
              @click="openScreenshot(screenshot.image)"
            >
              <img :src="screenshot.image" :alt="screenshot.desc" />
              <div class="screenshot-overlay">
                <i class="fas fa-search-plus"></i>
              </div>
              <p v-if="screenshot.desc" class="screenshot-desc">{{ screenshot.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../utils/axios'

const animeList = ref([])
const selectedAnime = ref(null)

const loadAnime = async () => {
  try {
    const data = await axios.get('/anime/')
    animeList.value = data.results || data
  } catch (error) {
    console.error('加载动漫失败:', error)
  }
}

const openAnimeDetail = (anime) => {
  selectedAnime.value = anime
  document.body.style.overflow = 'hidden'
}

const closeAnimeDetail = () => {
  selectedAnime.value = null
  document.body.style.overflow = 'auto'
}

const openScreenshot = (imageUrl) => {
  window.open(imageUrl, '_blank')
}

onMounted(() => {
  loadAnime()
})
</script>

<style scoped>
.anime-section {
  padding: 4rem 2rem;
  position: relative;
  z-index: 2;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.section-header i {
  font-size: 2.5rem;
  color: #FFB7C5;
}

.section-title {
  font-size: 2.5rem;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  margin: 0;
}

.anime-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 2rem;
}

.anime-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.anime-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 15px 40px rgba(255, 105, 180, 0.4);
}

.anime-cover {
  position: relative;
  width: 100%;
  height: 280px;
  overflow: hidden;
}

.anime-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.anime-card:hover .anime-cover img {
  transform: scale(1.1);
}

.anime-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0,0,0,0.3), transparent, rgba(0,0,0,0.7));
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1rem;
  opacity: 0;
  transition: opacity 0.3s;
}

.anime-card:hover .anime-overlay {
  opacity: 1;
}

.anime-rating {
  display: flex;
  gap: 3px;
}

.anime-rating i {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.9rem;
}

.anime-rating i.active {
  color: #FFD700;
}

.anime-year {
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
  text-align: right;
}

.anime-info {
  padding: 1rem;
}

.anime-name {
  font-size: 1.1rem;
  color: #333;
  margin-bottom: 0.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.anime-status {
  color: #FF69B4;
  font-size: 0.9rem;
}

/* 弹窗样式 */
.anime-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 2rem;
  overflow-y: auto;
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 1000px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  transition: all 0.3s;
  z-index: 10;
}

.close-btn:hover {
  background: #FF69B4;
  transform: rotate(90deg);
}

.modal-header {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.modal-cover {
  width: 180px;
  height: 260px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.modal-info {
  flex: 1;
}

.modal-info h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.modal-meta {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  opacity: 0.9;
}

.modal-rating {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 1rem;
}

.modal-rating i {
  color: rgba(255, 255, 255, 0.4);
  font-size: 1.3rem;
}

.modal-rating i.active {
  color: #FFD700;
}

.rating-text {
  margin-left: 0.5rem;
  font-size: 1.2rem;
  font-weight: bold;
}

.modal-desc {
  line-height: 1.8;
  font-size: 1rem;
}

.screenshots-section {
  padding: 2rem;
}

.screenshots-section h3 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.screenshots-section h3::before {
  content: '';
  width: 4px;
  height: 1.5rem;
  background: linear-gradient(135deg, #FFB7C5, #FF69B4);
  border-radius: 2px;
}

.screenshots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.screenshot-item {
  position: relative;
  cursor: pointer;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.screenshot-item:hover {
  transform: scale(1.05);
}

.screenshot-item img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.screenshot-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.screenshot-item:hover .screenshot-overlay {
  opacity: 1;
}

.screenshot-overlay i {
  color: white;
  font-size: 2rem;
}

.screenshot-desc {
  padding: 0.8rem;
  background: #f8f8f8;
  color: #666;
  font-size: 0.9rem;
  text-align: center;
}

@media (max-width: 768px) {
  .anime-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .modal-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .modal-cover {
    width: 150px;
    height: 220px;
  }
  
  .screenshots-grid {
    grid-template-columns: 1fr;
  }
}
</style>
