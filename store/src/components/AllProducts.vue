<template>
  <div>
    <div v-if="items.data" class="mt-4 grid grid-cols-1 md:grid-cols-4 gap-6 m-2 p-4">
      <div class="flex flex-col border border-neutral-200 rounded hover:shadow-lg max-w-[400px] " v-for="product in items.data.products" :key="product.item_name">
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

    <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
      <span v-for="page in totalPages" :key="page" :class="{ active: page === currentPage }" @click="goToPage(page)">
        {{ page }}
      </span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { Dialog, Button } from 'frappe-ui'
import { createResource } from 'frappe-ui'
import { session } from '../data/session'
import router from '../router';
import { useRoute } from 'vue-router';
import Product from '../components/Product.vue'

const currentPage = ref(1);
const itemsPerPage = ref(10);
const totalPages = ref(1);
const currentPageProducts = ref([]);

// Create the resource outside the watch function
const items = createResource({
  url: 'ecommerce.api.get_allproducts',
  auto: true,
});

// Watch for changes in currentPage
watch(currentPage, (newPage) => {
  items.params = {
    page: newPage,
    limit: itemsPerPage.value
  };
  fetchProducts();
});

onMounted(() => {
  fetchProducts();
});

const fetchProducts = async () => {
  const response = await items.fetch();
  console.log('Full Response:', response); // Check the entire response
  console.log('Total Count:', response.total_count); // Check the total count
  console.log('Products:', response.products); // Check the products data
  currentPageProducts.value = response.products;
  if (response.total_count && typeof response.total_count === 'number') {
    totalPages.value = Math.ceil(response.total_count / itemsPerPage.value);
  } else {
    totalPages.value = 1; // Or display an error message
  }
};

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const goToPage = (page) => {
  currentPage.value = page;
  fetchProducts();
};
</script>
