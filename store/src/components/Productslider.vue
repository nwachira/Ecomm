<template>
    <SfScrollable
      class="m-auto py-4 items-center w-full overflow-x-auto overflow-y-hidden"
      buttons-placement="floating"
      drag
      :items="limitedItems"
      scroll-direction="horizontal"
    >
      <template #previousButton="defaultProps">
        <SfButton
          v-bind="defaultProps"
          class="absolute !rounded-full z-10 left-4 bg-white hidden md:block"
          :class="{ '!hidden': defaultProps.disabled }"
          variant="secondary"
          size="lg"
          square
        >
          <SfIconChevronLeft />
        </SfButton>
      </template>
      <div class="flex gap-4"> <!-- Adjust gap value as per your design -->
        <div
          v-for="product in limitedItems"
          :key="product.item_code"
          class="first:ms-auto last:me-auto border border-neutral-200 shrink-0 rounded-md hover:shadow-lg w-[148px] lg:w-[192px]"
        >
          <div class="relative">
            <SfLink :href="`/product/${product.item_code}`" class="block">
              <img
                :src="product.image"
                :alt="product.name"
                class="block object-cover h-auto rounded-md aspect-square lg:w-[190px] lg:h-[190px]"
                width="146"
                height="146"
              />
            </SfLink>
            <SfButton
              variant="tertiary"
              size="sm"
              square
              class="absolute bottom-0 right-0 mr-2 mb-2 bg-white ring-1 ring-inset ring-neutral-200 !rounded-full"
              aria-label="Add to wishlist"
              @click="addProductToCart(product.item_name, product.image, product.item_code)"
            >
              <SfIconFavorite size="sm" />
            </SfButton>
          </div>
          <div class="p-2 border-t border-neutral-200 typography-text-sm">
            <SfLink :href="`/product/${product.item_code}`" variant="secondary" class="no-underline">{{ product.item_name }}</SfLink>
            <span class="block mt-2 font-bold">{{ product.price }}</span>
          </div>
        </div>
      </div>
      <template #nextButton="defaultProps">
        <SfButton
          v-bind="defaultProps"
          class="absolute !rounded-full z-10 right-4 bg-white hidden md:block"
          :class="{ '!hidden': defaultProps.disabled }"
          variant="secondary"
          size="lg"
          square
        >
          <SfIconChevronRight />
        </SfButton>
      </template>
    </SfScrollable>
  </template>
  
  <script setup>
  import { SfLink, SfButton, SfIconFavorite, SfIconChevronLeft, SfIconChevronRight, SfScrollable } from '@storefront-ui/vue';
  import { createResource } from 'frappe-ui';
  import { inject, computed } from 'vue';
  
  const cart = inject('cart');
  
  // Fetch products from backend API
  const items = createResource({
    url: 'ecommerce.api.get_products',
    auto: true,
  });
  
  // Computed property to slice the data
  const limitedItems = computed(() => {
    return items.data ? items.data.slice(0, 15) : [];
  });
  
  function addProductToCart(item_name, image, item_code) {
    // Add the product to the cart
    cart.items.push({
      product: item_name,
      qty: 1,
      image: image,
      item_code: item_code,
    });
  }
  </script>
  
  <style scoped>
  /* Add space between items */
  .flex > div {
    margin-right: 20px; /* Adjust as needed */
  }
  </style>
  