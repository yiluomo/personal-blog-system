<template>
  <div class="user-info-section">
    <div class="container">
      <div class="info-card">
        <div class="avatar-wrapper">
          <img :src="userInfo.avatar" :alt="userInfo.name" class="avatar" />
        </div>
        
        <h2 class="name">{{ userInfo.name }}</h2>
        <p class="intro">{{ userInfo.intro }}</p>
        
        <div class="resume-section">
          <h3 class="section-title">个人经历</h3>
          <div class="resume-list">
            <div 
              v-for="(item, index) in userInfo.resume_list" 
              :key="index"
              class="resume-item"
              :style="{ animationDelay: `${index * 0.2}s` }"
            >
              <i class="fas" :class="item.type === 'education' ? 'fa-graduation-cap' : 'fa-briefcase'"></i>
              <span>{{ item.content }}</span>
            </div>
          </div>
        </div>
        
        <div class="contact-section">
          <h3 class="section-title">联系方式</h3>
          <div class="contact-list">
            <a 
              v-for="(contact, index) in userInfo.contact_list" 
              :key="index"
              :href="contact.url"
              target="_blank"
              class="contact-item"
            >
              <i class="fas" :class="contact.icon"></i>
              <span>{{ contact.text }}</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../utils/axios'

const userInfo = ref({
  avatar: '',
  name: '',
  intro: '',
  resume_list: [],
  contact_list: []
})

const loadUserInfo = async () => {
  try {
    const data = await axios.get('/userinfo/current/')
    userInfo.value = data
  } catch (error) {
    console.error('加载用户信息失败:', error)
  }
}

onMounted(() => {
  loadUserInfo()
})
</script>

<style scoped>
.user-info-section {
  min-height: 100vh;
  padding: 4rem 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  max-width: 800px;
  width: 100%;
}

.info-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 3rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  animation: slideUp 1s ease-out;
}

.avatar-wrapper {
  text-align: center;
  margin-bottom: 2rem;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 5px solid #FFB7C5;
  transition: transform 0.3s;
}

.avatar:hover {
  transform: scale(1.1) rotate(5deg);
}

.name {
  text-align: center;
  font-size: 2rem;
  color: #333;
  margin-bottom: 1rem;
}

.intro {
  text-align: center;
  color: #666;
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.5rem;
  color: #FF69B4;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.section-title::before {
  content: '';
  width: 4px;
  height: 1.5rem;
  background: #FFB7C5;
  border-radius: 2px;
}

.resume-section {
  margin-bottom: 2rem;
}

.resume-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.resume-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(255, 183, 197, 0.1);
  border-radius: 10px;
  animation: fadeIn 0.8s ease-out both;
}

.resume-item i {
  color: #FF69B4;
  font-size: 1.5rem;
}

.contact-section {
  margin-top: 2rem;
}

.contact-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.5rem;
  background: linear-gradient(135deg, #FFB7C5, #FF69B4);
  color: white;
  border-radius: 25px;
  text-decoration: none;
  transition: all 0.3s;
}

.contact-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
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

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@media (max-width: 768px) {
  .info-card {
    padding: 2rem;
  }
  
  .name {
    font-size: 1.5rem;
  }
  
  .contact-list {
    flex-direction: column;
  }
}
</style>
