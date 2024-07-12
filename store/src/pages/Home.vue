<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Our Products</h1>
    <Product /> 
  </div>
  <pre>{{ items }}</pre>
</template>

<script setup>
import Product from '../components/Product.vue';
import { createResource } from 'frappe-ui';


const items = createResource({
url: 'ecommerce.api.get_products',
auto: true,
})
</script>
