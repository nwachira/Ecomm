<template>
  <div class="p-8 m-4 flex flex-wrap justify-center gap-4 md:justify-start md:gap-8">
    <div v-if="product.data" class=" flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 justify-between">
      <div v-for="item in product.data" :key="item.item_name"  class="">
        <div v-if="item.item_name === route.params.id" class=" md:flex md:justify-between md:gap-14 "> 
          <img :src="item.image" alt="" class="w-full h-80  rounded-sm"> <div class=" md:w-1/2 mt-6">
            <h2 class="text-xl font-bold">{{ item.item_description }}</h2>
            <div class="prose prose-sm max-w-prose"> <p class="text-gray-600 mt-2" v-html="item.description"></p> </div>
            <Button class="mt-4">Add to Cart</Button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { createResource } from 'frappe-ui';
import { useRoute } from 'vue-router';

const route = useRoute();
const product = createResource({
  url: `ecommerce.api.get_products`, // Fetch all products
  auto: true,
});

// For debugging
console.log('Product data:', product);
</script>
