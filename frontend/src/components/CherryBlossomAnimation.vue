<template>
  <div class="cherry-blossom-container"></div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue'
import anime from 'animejs'

let animationInterval = null

const createPetal = () => {
  const container = document.querySelector('.cherry-blossom-container')
  if (!container) return

  const petal = document.createElement('div')
  petal.className = 'petal'
  
  const size = Math.random() * 10 + 5
  const startX = Math.random() * window.innerWidth
  const endX = startX + (Math.random() - 0.5) * 200
  const duration = Math.random() * 5000 + 8000
  const delay = Math.random() * 1000
  
  petal.style.cssText = `
    position: fixed;
    width: ${size}px;
    height: ${size}px;
    background: radial-gradient(circle, #FFB7C5, #FFC0CB);
    border-radius: 50% 0 50% 0;
    opacity: ${Math.random() * 0.5 + 0.3};
    left: ${startX}px;
    top: -20px;
    pointer-events: none;
    z-index: 1;
  `
  
  container.appendChild(petal)
  
  anime({
    targets: petal,
    translateY: window.innerHeight + 50,
    translateX: endX - startX,
    rotate: Math.random() * 720,
    opacity: [
      { value: Math.random() * 0.5 + 0.3, duration: duration * 0.2 },
      { value: 0, duration: duration * 0.8 }
    ],
    duration: duration,
    delay: delay,
    easing: 'linear',
    complete: () => {
      if (petal.parentNode) {
        petal.parentNode.removeChild(petal)
      }
    }
  })
}

onMounted(() => {
  const petalCount = window.innerWidth > 768 ? 20 : 10
  
  for (let i = 0; i < petalCount; i++) {
    setTimeout(() => createPetal(), i * 300)
  }
  
  animationInterval = setInterval(() => {
    createPetal()
  }, 800)
})

onUnmounted(() => {
  if (animationInterval) {
    clearInterval(animationInterval)
  }
})
</script>

<style scoped>
.cherry-blossom-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}
</style>
