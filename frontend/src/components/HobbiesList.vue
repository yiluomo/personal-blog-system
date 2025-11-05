<template>
  <div class="hobbies-section">
    <div class="container">
      <h2 class="main-title">我的爱好</h2>
      
      <!-- 标签页导航 -->
      <div class="tabs-nav">
        <button 
          v-for="tab in tabs" 
          :key="tab.type"
          class="tab-btn"
          :class="{ active: activeTab === tab.type }"
          @click="activeTab = tab.type"
        >
          <i class="fas" :class="tab.icon"></i>
          <span>{{ tab.name }}</span>
        </button>
      </div>

      <!-- 标签页内容 -->
      <div class="tabs-content">
        <transition name="fade" mode="out-in">
          <GamesList v-if="activeTab === 'game'" :key="'game'" />
          <MusicPlayer v-else-if="activeTab === 'music'" :key="'music'" />
          <AnimeList v-else-if="activeTab === 'anime'" :key="'anime'" />
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GamesList from './GamesList.vue'
import MusicPlayer from './MusicPlayer.vue'
import AnimeList from './AnimeList.vue'

const activeTab = ref('game')

const tabs = [
  { type: 'game', name: '游戏', icon: 'fa-gamepad' },
  { type: 'music', name: '音乐', icon: 'fa-music' },
  { type: 'anime', name: '动漫', icon: 'fa-film' }
]
</script>

<style scoped>
.hobbies-section {
  min-height: 100vh;
  padding: 4rem 2rem;
  position: relative;
  z-index: 2;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
}

.main-title {
  text-align: center;
  font-size: 3rem;
  color: white;
  margin-bottom: 3rem;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  animation: fadeIn 1s ease-out;
}

.tabs-nav {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 3rem;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 1rem 2.5rem;
  background: rgba(255, 255, 255, 0.9);
  border: 3px solid transparent;
  border-radius: 50px;
  color: #666;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.tab-btn i {
  font-size: 1.3rem;
}

.tab-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(255, 105, 180, 0.3);
  border-color: #FFB7C5;
}

.tab-btn.active {
  background: linear-gradient(135deg, #FFB7C5, #FF69B4);
  color: white;
  border-color: #FF69B4;
  box-shadow: 0 8px 25px rgba(255, 105, 180, 0.5);
  transform: translateY(-3px);
}

.tabs-content {
  position: relative;
  min-height: 400px;
}

/* 过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .main-title {
    font-size: 2rem;
  }
  
  .tabs-nav {
    flex-direction: column;
    align-items: stretch;
  }
  
  .tab-btn {
    justify-content: center;
  }
}
</style>
