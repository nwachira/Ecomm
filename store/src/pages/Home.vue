<template>
  <Banner />

    <div class=" m-4">
  <div class=" ">
      <h1 class="text-3xl font-bold mb-4 p-4">Our Products</h1>

    </div>
   
    <Product /> 
  </div>
  <Herowithrightimage />

  <Productslider />
  
</template>

<script setup>
import Product from '../components/Product.vue';
import { createResource } from 'frappe-ui';
import { SfButton } from '@storefront-ui/vue';
import Banner from '../components/Banner.vue';
import Herowithrightimage from '../components/Herowithrightimage.vue';
import Productslider from '../components/Productslider.vue';





const items = createResource({
url: 'ecommerce.api.get_products',
auto: true,
})
</script>
