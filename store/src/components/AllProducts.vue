<template>
  <div class=" mx-6">

 
  <div class="flex ">
    <div  class="w-1/4">
      <h1>Filters</h1>
    </div>
    <!-- Products grid -->
    <div v-if="items.data && items.data.products" class="mt-4 grid grid-cols-1 md:grid-cols-4 gap-6 m-2 p-4 w-3/4">
      <div class="flex flex-col border border-neutral-200 rounded hover:shadow-lg max-w-[400px]" v-for="product in items.data.products" :key="product.item_name">
        <router-link :to="`/product/${product.item_name}`">
          <img :src="product.image" alt="" 
            class="block object-cover h-auto rounded-md aspect-square"
            width="400"
            height="400">
          <div class="p-4 border-t border-neutral-200">
            <p>{{ product.item_description }}</p>
          </div>
        </router-link>
        <div class="mx-4 mb-4 flex justify-between items-center">
          <SfButton
            size="sm"
            @click="addProductToCart(product.item_name, product.image, product.item_code)"
          >
            <template #prefix>
              <SfIconShoppingCart size="sm" />
            </template>
            Add to cart
          </SfButton>
        </div>
      </div>
    </div>

  
    
  </div>
    <!-- Pagination -->
  <div class="pagination flex justify-center items-center gap-4">
    <button
      :class="[
        'min-w-[38px] px-3 sm:px-4 py-3 md:w-12 text-neutral-500 rounded-md hover:bg-primary-100 hover:text-primary-800 active:bg-primary-200 active:text-primary-900',
        { '!text-neutral-900 hover:!text-primary-800 active:!text-primary-900': currentPage === 1 },
      ]"
      @click="previousPage"
      :disabled="currentPage === 1"
    >
      Previous
    </button>

    <div class="flex gap-2 mx-4 my-4">
      <span
        v-for="page in totalPages"
        :key="page"
        :class="[
          'mx-2 cursor-pointer',
          { 'active': page === currentPage }
        ]"
        @click="goToPage(page)"
      >
        {{ page }}
      </span>
    </div>

    <button
      :class="[
        'min-w-[38px] px-3 sm:px-4 py-3 md:w-12 text-neutral-500 rounded-md hover:bg-primary-100 hover:text-primary-800 active:bg-primary-200 active:text-primary-900',
        { '!text-neutral-900 hover:!text-primary-800 active:!text-primary-900': currentPage === totalPages },
      ]"
      @click="nextPage"
      :disabled="currentPage === totalPages"
    >
      Next
    </button>
  </div>
</div>
</template>


<script setup>
import { ref, computed, onMounted, watch, inject } from 'vue'
import { createResource } from 'frappe-ui'
import { useRoute } from 'vue-router'
import { SfButton, SfIconShoppingCart } from '@storefront-ui/vue'

const route = useRoute()

const currentPage = ref(1)
const itemsPerPage = ref(10)
const totalPages = ref(1)
const currentPageProducts = ref([])
const cart = inject('cart')

// Create the resource for fetching products
const items = createResource({
  url: 'ecommerce.api.get_allproducts',
  auto: true,
})

// Watch for changes in currentPage
watch(currentPage, (newPage) => {
  items.params = {
    page: newPage,
    limit: itemsPerPage.value
  }
  fetchProducts()
})

// Fetch products on component mount
onMounted(() => {
  fetchProducts()
})

// Function to fetch products based on current page and limit
const fetchProducts = async () => {
  try {
    const response = await items.fetch()
    console.log('Full Response:', response) // Check the entire response
    console.log('Total Count:', response.total_count) // Check the total count
    console.log('Products:', response.products) // Check the products data
    currentPageProducts.value = response.products
    totalPages.value = Math.ceil(response.total_count / itemsPerPage.value)
  } catch (error) {
    console.error('Error fetching products:', error)
  }
}

// Function to navigate to previous page
const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

// Function to navigate to next page
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

// Function to navigate to specific page
const goToPage = (page) => {
  currentPage.value = page
  fetchProducts()
}

// Function to add product to cart
function addProductToCart(item_name, image) {
  // Find the product in currentPageProducts that matches the item_description
  const product = currentPageProducts.value.find(
    (product) => product.item_name === item_name
  )

  if (product) {
    // Add the product to the cart with its actual name
    cart.items.push({
      product: item_name, 
      qty: 1,
      image: image,
    })
  } else {
    console.error(`Product with name ${item_name} not found.`)
  }
}
</script>


<style scoped>
.active {
  background-color: #3182ce; /* Example background color for active page */
  color: white; /* Example text color for active page */
  border-radius: 4px; /* Example border radius */
  padding: 5px 10px; /* Example padding */
}
</style>
