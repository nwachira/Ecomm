<template>
    <div class="flex flex-col md:flex-row flex-wrap gap-6 max-w-[1840px] md:mr-6 md:ml-4" v-if="bannerData">

        <pre></pre>
      <div
        v-for="banner in bannerData"
        :key="banner.title"
        :class="[
          'relative flex md:max-w-[906px] md:[&:not(:first-of-type)]:flex-1 md:first-of-type:w-full border ',
           banner.background_color,
        ]"
      >
        <a
          class="absolute w-full h-full z-1 focus-visible:outline focus-visible:rounded-lg"
          :aria-label="banner.title"
          :href="banner.route"
        />
        <div :class="['flex justify-between overflow-hidden grow', { 'flex-row-reverse': banner.reverse === 'true' }]">
          <div class="flex flex-col justify-center items-start p-6 lg:p-10 max-w-1/2">
            <p :class="['uppercase typography-text-xs block font-bold tracking-widest', banner.subtitle_class]">
              {{ banner.subtitle }}
            </p>
            <h2 :class="['mb-4 mt-2 font-bold typography-display-3', banner.title_class]">
              {{ banner.title }}
            </h2>
            <p class="typography-text-base block mb-4">
              {{ banner.description }}
            </p>
            <Button class="" size="lg"  variant="solid">{{ banner.button_label }}</Button>
          </div>
          <img :src="banner.image" :alt="banner.title" class="w-1/2 self-end object-contain" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { createResource } from 'frappe-ui';
  import { SfButton } from '@storefront-ui/vue';
  import { Button } from 'frappe-ui'
  
  export default {
    data() {
      return {
        banner: createResource({
          url: 'ecommerce.api.get_banner',
          auto: true,
        }),
      };
    },
    computed: {
      bannerData() {
        if (this.banner.data) {
          return this.banner.data;
        } else {
          return null;
        }
      },
    },
  };
  </script>
  