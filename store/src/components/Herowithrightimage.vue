<template>
    <div v-if="hero.data" class="relative min-h-[576px]">
        <div v-for="heros in hero.data" class="relative">

        
      <picture>
        <source :srcset="hero.background_image" media="(min-width: 768px)" />
        <img
          :src="heros.phone_image"
          class="absolute w-full h-full z-[-1] object-cover"
          alt="hero"
        />
      </picture>
      <div class="md:flex md:flex-row-reverse md:justify-center max-w-[1536px] mx-auto min-h-[576px]">
        <div class="flex flex-col md:basis-2/4 md:items-stretch md:overflow-hidden">
          <img
            
            :src="heros.image"
            alt="Headphones"
            class="h-full w-full object-cover object-left"
          />
          
        </div>
        <div class="p-4 md:p-10 md:max-w-[768px] md:flex md:flex-col md:justify-center md:items-start md:basis-2/4">
          <p class="typography-text-xs md:typography-text-sm font-bold tracking-widest text-neutral-500 uppercase">
            {{ heros.subtitle }}
          </p>
          <h1 class="typography-display-2 md:typography-display-1 md:leading-[67.5px] font-bold mt-2 mb-4">
            {{ heros.title }}
          </h1>
          <p class="typography-text-base md:typography-text-lg">
            {{ heros.description }}
          </p>
          <div class="flex flex-col md:flex-row gap-4 mt-6">
            <SfButton size="lg"> {{ heros.button_label }} </SfButton>
            <SfButton size="lg" variant="secondary" class="bg-white"> {{ heros.button_label1 }} </SfButton>
          </div>
        </div>
      </div>
    </div>
    </div>
  </template>
  
  <script setup>
  import { createResource } from 'frappe-ui';
  import { SfButton } from '@storefront-ui/vue';
  
  const hero = createResource({
    url: 'ecommerce.api.get_hero',
    auto: true,
  });
  </script>
  