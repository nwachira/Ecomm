<template>

  <div class=" ">
    <h1 class="text-3xl font-bold mb-4">Our Products</h1>
    <Product /> 
  </div>
  
</template>

<script setup>
import Product from '../components/Product.vue';
import { createResource } from 'frappe-ui';
import { SfButton } from '@storefront-ui/vue';


const items = createResource({
url: 'ecommerce.api.get_products',
auto: true,
})
</script>
