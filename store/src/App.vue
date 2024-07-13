<template>
 
  <div>
    <Navbar />
    <router-view />
    <Footer />
  </div>
 
</template>
<script setup>
  import Navbar from './components/Navbar.vue'
  import Footer from './components/Footer.vue'
  import { inject } from 'vue'
  import { watch } from 'vue'


  const cart = inject("cart")

watch(cart.items, () => {
	console.log("watcher works!")
	// update cart in local storage
	localStorage.setItem("cart", JSON.stringify(cart))
})
</script>
