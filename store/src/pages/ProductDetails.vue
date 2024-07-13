<template>
  <div class="p-8 m-4 flex flex-wrap justify-center gap-4 md:justify-start md:gap-8">
    <div v-if="productResource.data" class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 justify-between">
      <div v-for="item in productResource.data" :key="item.item_name" class="">
        <div v-if="item.item_name === route.params.id" class="md:flex md:justify-between md:gap-14">
          <img :src="item.image" alt="" class="w-full h-80 rounded-sm">
          <div class="md:w-1/2 mt-6">
            <h2 class="text-xl font-bold">{{ item.item_description }}</h2>
            <div class="prose prose-sm max-w-prose">
              <p class="text-gray-600 mt-2" v-html="item.description"></p>
            </div>
            <div class="mx-4 mb-4 flex justify-between items-center">
              <SfButton
                size="sm"
                @click="addProductToCart(item.item_description, item.image)"
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
    </div>
  </div>
</template>

<script setup>
import { createResource } from 'frappe-ui';
import { useRoute } from 'vue-router';
import { inject } from 'vue';
import { SfButton, SfIconShoppingCart } from '@storefront-ui/vue';

const route = useRoute();
const productResource = createResource({
  url: 'ecommerce.api.get_products', // Fetch all products
  auto: true,
});
const cart = inject("cart");

function addProductToCart(item_description, image) {
  // Use productResource.data to access the data after it's loaded
  const foundProduct = productResource.data.find(product => product.item_description === item_description);

  if (foundProduct) {
    // Add the product to the cart with its name
    cart.items.push({
      product: item_description, // Use the actual product name
      qty: 1,
      image: image,
    });
  } else {
    console.error(`Product with name ${item_description} not found.`);
  }
}
</script>
