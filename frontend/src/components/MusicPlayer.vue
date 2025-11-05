<template>
  <div class="music-section">
    <div class="container">
      <div class="section-header">
        <i class="fas fa-music"></i>
        <h2 class="section-title">音乐收藏</h2>
      </div>

      <div class="music-player-wrapper">
        <!-- 当前播放信息 -->
        <div class="now-playing" v-if="currentMusic">
          <div class="album-cover-container">
            <div class="album-cover" :class="{ rotating: isPlaying }">
              <img :src="currentMusic.cover" :alt="currentMusic.title" />
            </div>
            <div class="needle" :class="{ playing: isPlaying }"></div>
          </div>
          
          <div class="music-info">
            <h3 class="music-title">{{ currentMusic.title }}</h3>
            <p class="music-artist">{{ currentMusic.artist }}</p>
            <p v-if="currentMusic.album" class="music-album">专辑: {{ currentMusic.album }}</p>
          </div>
        </div>

        <!-- 播放控制 -->
        <div class="player-controls" v-if="currentMusic">
          <div class="progress-bar">
            <span class="time">{{ formatTime(currentTime) }}</span>
            <div class="progress-track" @click="seek">
              <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
              <div class="progress-thumb" :style="{ left: progressPercent + '%' }"></div>
            </div>
            <span class="time">{{ currentMusic.duration }}</span>
          </div>
          
          <div class="control-buttons">
            <button @click="prevSong" class="control-btn">
              <i class="fas fa-step-backward"></i>
            </button>
            <button @click="togglePlay" class="control-btn play-btn">
              <i class="fas" :class="isPlaying ? 'fa-pause' : 'fa-play'"></i>
            </button>
            <button @click="nextSong" class="control-btn">
              <i class="fas fa-step-forward"></i>
            </button>
            <button @click="toggleMute" class="control-btn volume-btn">
              <i class="fas" :class="isMuted ? 'fa-volume-mute' : 'fa-volume-up'"></i>
            </button>
          </div>
        </div>

        <!-- 播放列表 -->
        <div class="playlist">
          <h3 class="playlist-title">
            <i class="fas fa-list"></i> 播放列表 ({{ musicList.length }})
          </h3>
          <div class="playlist-items">
            <div 
              v-for="(music, index) in musicList" 
              :key="music.id"
              class="playlist-item"
              :class="{ active: currentMusic && currentMusic.id === music.id }"
              @click="playMusic(index)"
            >
              <div class="item-index">
                <span v-if="currentMusic && currentMusic.id === music.id && isPlaying">
                  <i class="fas fa-volume-up playing-icon"></i>
                </span>
                <span v-else>{{ String(index + 1).padStart(2, '0') }}</span>
              </div>
              <div class="item-cover">
                <img :src="music.cover" :alt="music.title" />
              </div>
              <div class="item-info">
                <p class="item-title">{{ music.title }}</p>
                <p class="item-artist">{{ music.artist }}</p>
              </div>
              <div class="item-duration">{{ music.duration }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 隐藏的音频元素 -->
    <audio 
      ref="audioPlayer" 
      @timeupdate="updateProgress"
      @ended="nextSong"
      @loadedmetadata="onAudioLoaded"
    ></audio>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import axios from '../utils/axios'

const musicList = ref([])
const currentMusic = ref(null)
const currentIndex = ref(0)
const isPlaying = ref(false)
const isMuted = ref(false)
const currentTime = ref(0)
const duration = ref(0)
const audioPlayer = ref(null)

const progressPercent = computed(() => {
  if (duration.value === 0) return 0
  return (currentTime.value / duration.value) * 100
})

const loadMusic = async () => {
  try {
    const data = await axios.get('/music/')
    musicList.value = data.results || data
    if (musicList.value.length > 0) {
      currentMusic.value = musicList.value[0]
      loadAudio()
    }
  } catch (error) {
    console.error('加载音乐失败:', error)
  }
}

const loadAudio = () => {
  if (audioPlayer.value && currentMusic.value) {
    audioPlayer.value.src = currentMusic.value.audio_url
    audioPlayer.value.load()
  }
}

const playMusic = (index) => {
  currentIndex.value = index
  currentMusic.value = musicList.value[index]
  loadAudio()
  setTimeout(() => {
    audioPlayer.value.play()
    isPlaying.value = true
  }, 100)
}

const togglePlay = () => {
  if (!audioPlayer.value) return
  
  if (isPlaying.value) {
    audioPlayer.value.pause()
  } else {
    audioPlayer.value.play()
  }
  isPlaying.value = !isPlaying.value
}

const prevSong = () => {
  currentIndex.value = (currentIndex.value - 1 + musicList.value.length) % musicList.value.length
  playMusic(currentIndex.value)
}

const nextSong = () => {
  currentIndex.value = (currentIndex.value + 1) % musicList.value.length
  playMusic(currentIndex.value)
}

const toggleMute = () => {
  if (audioPlayer.value) {
    audioPlayer.value.muted = !audioPlayer.value.muted
    isMuted.value = audioPlayer.value.muted
  }
}

const updateProgress = () => {
  if (audioPlayer.value) {
    currentTime.value = audioPlayer.value.currentTime
  }
}

const onAudioLoaded = () => {
  if (audioPlayer.value) {
    duration.value = audioPlayer.value.duration
  }
}

const seek = (event) => {
  if (!audioPlayer.value) return
  const progressBar = event.currentTarget
  const clickX = event.offsetX
  const width = progressBar.offsetWidth
  const seekTime = (clickX / width) * duration.value
  audioPlayer.value.currentTime = seekTime
}

const formatTime = (seconds) => {
  if (isNaN(seconds)) return '00:00'
  const mins = Math.floor(seconds / 60)
  const secs = Math.floor(seconds % 60)
  return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`
}

onMounted(() => {
  loadMusic()
})

onUnmounted(() => {
  if (audioPlayer.value) {
    audioPlayer.value.pause()
  }
})
</script>

<style scoped>
.music-section {
  padding: 4rem 2rem;
  position: relative;
  z-index: 2;
}

.container {
  max-width: 1000px;
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

.music-player-wrapper {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

/* 当前播放 */
.now-playing {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid #f0f0f0;
}

.album-cover-container {
  position: relative;
  width: 200px;
  height: 200px;
}

.album-cover {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  position: relative;
}

.album-cover::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40px;
  height: 40px;
  background: rgba(0, 0, 0, 0.8);
  border-radius: 50%;
  z-index: 2;
}

.album-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.album-cover.rotating {
  animation: rotate 20s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.needle {
  position: absolute;
  top: -10px;
  right: 40px;
  width: 100px;
  height: 100px;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><line x1="10" y1="10" x2="90" y2="90" stroke="%23333" stroke-width="3"/><circle cx="10" cy="10" r="8" fill="%23666"/></svg>') no-repeat;
  background-size: contain;
  transform-origin: 10px 10px;
  transform: rotate(-30deg);
  transition: transform 0.5s;
  z-index: 3;
}

.needle.playing {
  transform: rotate(0deg);
}

.music-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.music-title {
  font-size: 2rem;
  color: #333;
  margin-bottom: 0.5rem;
}

.music-artist {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.music-album {
  color: #999;
}

/* 播放控制 */
.player-controls {
  margin-bottom: 2rem;
}

.progress-bar {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.time {
  color: #666;
  font-size: 0.9rem;
  min-width: 45px;
}

.progress-track {
  flex: 1;
  height: 6px;
  background: #e0e0e0;
  border-radius: 3px;
  position: relative;
  cursor: pointer;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #FFB7C5, #FF69B4);
  border-radius: 3px;
  transition: width 0.1s;
}

.progress-thumb {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
  background: #FF69B4;
  border-radius: 50%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.control-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;
}

.control-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: none;
  background: #f5f5f5;
  color: #333;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.control-btn:hover {
  background: #FFB7C5;
  color: white;
  transform: scale(1.1);
}

.play-btn {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #FFB7C5, #FF69B4);
  color: white;
  font-size: 1.5rem;
}

.play-btn:hover {
  transform: scale(1.15);
  box-shadow: 0 5px 20px rgba(255, 105, 180, 0.5);
}

/* 播放列表 */
.playlist {
  margin-top: 2rem;
}

.playlist-title {
  font-size: 1.3rem;
  color: #333;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.playlist-title i {
  color: #FFB7C5;
}

.playlist-items {
  max-height: 400px;
  overflow-y: auto;
}

.playlist-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s;
}

.playlist-item:hover {
  background: #f8f8f8;
}

.playlist-item.active {
  background: linear-gradient(90deg, rgba(255, 183, 197, 0.2), rgba(255, 105, 180, 0.2));
}

.item-index {
  width: 30px;
  text-align: center;
  color: #999;
  font-weight: bold;
}

.playing-icon {
  color: #FF69B4;
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.item-cover {
  width: 50px;
  height: 50px;
  border-radius: 5px;
  overflow: hidden;
}

.item-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-info {
  flex: 1;
}

.item-title {
  color: #333;
  font-weight: 500;
  margin-bottom: 0.3rem;
}

.item-artist {
  color: #999;
  font-size: 0.9rem;
}

.item-duration {
  color: #999;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .now-playing {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .album-cover-container {
    width: 150px;
    height: 150px;
  }
  
  .control-buttons {
    gap: 1rem;
  }
  
  .control-btn {
    width: 45px;
    height: 45px;
  }
  
  .play-btn {
    width: 55px;
    height: 55px;
  }
}
</style>
