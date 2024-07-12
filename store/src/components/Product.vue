<template>
  <div v-if="items.data" class="mt-4 grid grid-cols-1 md:grid-cols-4 gap-6 m-2 p-4">
      <div class="flex flex-col border border-neutral-200 rounded hover:shadow-lg max-w-[400px] " v-for="product in limitedItems" :key="product.item_name">
          <router-link :to="`/product/${product.item_name}`">

          <img :src="product.image" alt="" 
          class="block object-cover h-auto rounded-md aspect-square"
          width="400"
          height="400">
          <div class="p-4 border-t border-neutral-200">
            <p>{{ product.item_description }}</p>
            <Button >Add to Cart</Button>

          </div>
          
         
      </router-link>
      </div>


  </div>



</template>
<script setup>
import { ref, computed } from 'vue'
import { Dialog, Button } from 'frappe-ui'
import { createResource } from 'frappe-ui'
import { session } from '../data/session'
import router from '../router';
import { useRoute } from 'vue-router';
import Product from './Product.vue'



const ping = createResource({
url: 'ping',
auto: true,
})
const items = createResource({
url: 'ecommerce.api.get_products',
auto: true,
})

// Computed property to slice the data
const limitedItems = computed(() => {
return items.data ? items.data.slice(0, 8) : [];
});

</script>
