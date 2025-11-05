<template>
  <div class="games-section">
    <div class="container">
      <div class="section-header">
        <i class="fas fa-gamepad"></i>
        <h2 class="section-title">游戏收藏</h2>
      </div>
      
      <div class="games-grid">
        <div 
          v-for="game in games" 
          :key="game.id"
          class="game-card"
          @click="openGameDetail(game)"
        >
          <div class="game-cover">
            <img :src="game.cover" :alt="game.name" />
            <div class="game-rating">
              <i v-for="n in 5" :key="n" class="fas fa-star" :class="{ active: n <= game.rating }"></i>
            </div>
          </div>
          <div class="game-info">
            <h3 class="game-name">{{ game.name }}</h3>
            <p class="game-desc">{{ game.desc }}</p>
            <div class="game-meta">
              <span v-if="game.play_time" class="play-time">
                <i class="fas fa-clock"></i> {{ game.play_time }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 游戏详情弹窗 -->
    <div v-if="selectedGame" class="game-modal" @click="closeGameDetail">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="closeGameDetail">
          <i class="fas fa-times"></i>
        </button>
        
        <div class="modal-header">
          <img :src="selectedGame.cover" :alt="selectedGame.name" class="modal-cover" />
          <div class="modal-info">
            <h2>{{ selectedGame.name }}</h2>
            <div class="modal-rating">
              <i v-for="n in 5" :key="n" class="fas fa-star" :class="{ active: n <= selectedGame.rating }"></i>
            </div>
            <p class="modal-desc">{{ selectedGame.desc }}</p>
            <p v-if="selectedGame.play_time" class="modal-time">
              <i class="fas fa-clock"></i> 游玩时长: {{ selectedGame.play_time }}
            </p>
          </div>
        </div>
        
        <div v-if="selectedGame.screenshots && selectedGame.screenshots.length" class="screenshots-section">
          <h3>游戏截图</h3>
          <div class="screenshots-grid">
            <div 
              v-for="screenshot in selectedGame.screenshots" 
              :key="screenshot.id"
              class="screenshot-item"
              @click="openScreenshot(screenshot.image)"
            >
              <img :src="screenshot.image" :alt="screenshot.desc" />
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

const games = ref([])
const selectedGame = ref(null)

const loadGames = async () => {
  try {
    const data = await axios.get('/games/')
    games.value = data.results || data
  } catch (error) {
    console.error('加载游戏失败:', error)
  }
}

const openGameDetail = (game) => {
  selectedGame.value = game
  document.body.style.overflow = 'hidden'
}

const closeGameDetail = () => {
  selectedGame.value = null
  document.body.style.overflow = 'auto'
}

const openScreenshot = (imageUrl) => {
  window.open(imageUrl, '_blank')
}

onMounted(() => {
  loadGames()
})
</script>

<style scoped>
.games-section {
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

.games-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}

.game-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.game-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(255, 105, 180, 0.4);
}

.game-cover {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.game-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.game-card:hover .game-cover img {
  transform: scale(1.1);
}

.game-rating {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.7);
  padding: 5px 10px;
  border-radius: 20px;
  display: flex;
  gap: 3px;
}

.game-rating i {
  color: #ddd;
  font-size: 0.8rem;
}

.game-rating i.active {
  color: #FFD700;
}

.game-info {
  padding: 1.5rem;
}

.game-name {
  font-size: 1.3rem;
  color: #333;
  margin-bottom: 0.5rem;
}

.game-desc {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.game-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
  color: #999;
  font-size: 0.9rem;
}

.play-time i {
  color: #FFB7C5;
}

/* 弹窗样式 */
.game-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
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
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.5);
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
  background: linear-gradient(135deg, #FFB7C5, #FF69B4);
  color: white;
}

.modal-cover {
  width: 200px;
  height: 280px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.modal-info {
  flex: 1;
}

.modal-info h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.modal-rating {
  display: flex;
  gap: 5px;
  margin-bottom: 1rem;
}

.modal-rating i {
  color: rgba(255, 255, 255, 0.5);
  font-size: 1.2rem;
}

.modal-rating i.active {
  color: #FFD700;
}

.modal-desc {
  line-height: 1.8;
  margin-bottom: 1rem;
}

.modal-time {
  font-size: 1.1rem;
  opacity: 0.9;
}

.screenshots-section {
  padding: 2rem;
}

.screenshots-section h3 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1.5rem;
}

.screenshots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.screenshot-item {
  cursor: pointer;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s;
}

.screenshot-item:hover {
  transform: scale(1.05);
}

.screenshot-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
}

.screenshot-desc {
  padding: 0.5rem;
  background: #f5f5f5;
  text-align: center;
  color: #666;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .games-grid {
    grid-template-columns: 1fr;
  }
  
  .modal-header {
    flex-direction: column;
    align-items: center;
  }
  
  .modal-cover {
    width: 150px;
    height: 210px;
  }
  
  .screenshots-grid {
    grid-template-columns: 1fr;
  }
}
</style>
