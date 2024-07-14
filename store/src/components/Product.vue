<template>
  <div v-if="items.data" class="mt-4 sm:grid-cols-3  grid grid-cols-1 md:grid-cols-6 gap-6 m-2 p-4 place-items-center">
    <div
      class="flex flex-col border border-neutral-200 rounded hover:shadow-lg max-w-[400px]"
      v-for="product in limitedItems"
      :key="product.item_name"
    >
      <router-link :to="`/product/${product.item_name}`">
        <img
          :src="product.image"
          alt=""
          class="block object-cover h-auto rounded-md aspect-square"
          width="400"
          height="400"
        />
        <div class="p-4 border-t border-neutral-200">
          <p>{{ product.item_description }}</p>
        </div>
      </router-link>
      <div class="mx-4 mb-4 flex justify-between items-center">
        <SfButton
          size="sm"
          @click="addProductToCart(product.item_name, product.image, product.item_code)">
          <template #prefix>
            <SfIconShoppingCart size="sm" />
          </template>
          Add to cart
        </SfButton>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, inject } from "vue";
import { createResource } from "frappe-ui";
import { session } from "../data/session";
import router from "../router";
import { useRoute } from "vue-router";
import {
  SfRating,
  SfCounter,
  SfLink,
  SfButton,
  SfIconShoppingCart,
  SfIconFavorite,
} from "@storefront-ui/vue";

const cart = inject("cart");

const ping = createResource({
  url: "ping",
  auto: true,
});
const items = createResource({
  url: "ecommerce.api.get_products",
  auto: true,
});

// Computed property to slice the data
const limitedItems = computed(() => {
  return items.data ? items.data.slice(0, 8) : [];
});
const route = useRoute();
function addProductToCart(item_name, image, item_code) { // Add item_code as a parameter
  // Find the product in items.data that matches the item_name
  const product = items.data.find(
    (product) => product.item_name === item_name // Use item_name for comparison
  );

  if (product) {
    // Add the product to the cart with its name
    cart.items.push({
      product: item_name, // Use the actual product name
      qty: 1,
      image: image,
      item_code: item_code // Include item_code in the cart item
    });
  } else {
    console.error(`Product with name ${item_name} not found.`);
  }
}
</script>
