<template>
  <div class="home-view">
    <Carousel />
    <UserInfoCard />
    <WorksList />
    <HobbiesList />
    <footer class="footer">
      <p>&copy; 2024 樱花博客 | 用心记录生活</p>
    </footer>
  </div>
</template>

<script setup>
import Carousel from '../components/Carousel.vue'
import UserInfoCard from '../components/UserInfoCard.vue'
import WorksList from '../components/WorksList.vue'
import HobbiesList from '../components/HobbiesList.vue'
</script>

<style scoped>
.home-view {
  position: relative;
  z-index: 2;
}

.footer {
  background: rgba(0, 0, 0, 0.5);
  color: white;
  text-align: center;
  padding: 2rem;
  backdrop-filter: blur(10px);
}

.footer p {
  margin: 0;
  font-size: 0.9rem;
}
</style>
