<template>
    <footer class="bg-gray-900 text-white py-8 ">
        <div class="container mx-auto px-4">
          <template v-if="footeritems.loading">
            <div class="loading-indicator">Loading footer...</div>
          </template>
          <template v-else-if="footeritems.error">
            <div class="error-message">Error loading footer.</div>
          </template>
          <template v-else-if="footeritems.data">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-10 px-4 cursor-pointer ">
              <div v-for="(parent, parentLabel) in groupedFooterItems" :key="parentLabel">
                <h3 class="text-lg font-bold mb-4">{{ parentLabel }}</h3>
                <ul>
                  <li v-for="item in parent" :key="item.name">
                    <a :href="item.url" class="hover:text-amber-200">{{ item.label }}</a>
                  </li>
                </ul>
              </div>
            </div>
    
            <div class="mt-8 flex flex-wrap gap-4  justify-between items-center cursor-pointer">
              <p class="text-sm">
                &copy; {{ footeritems.data.copyright }} - {{ footeritems.data.address }}
              </p>
              <p class="text-sm">
                Powered by {{ footeritems.data.footer_powered }}
              </p>
            </div>
          </template>
        </div>
      </footer>
  </template>
  
  <script setup>
  import { createResource } from 'frappe-ui'
  import { computed } from 'vue'
  
  const footeritems = createResource({
    url: 'ecommerce.api.get_items',
    auto: true,
  });
  
  const groupedFooterItems = computed(() => {
    if (footeritems.data) {
      const grouped = {};
      footeritems.data.footer_items.forEach(item => {
        const parentLabel = item.parent_label || item.label;
        if (!grouped[parentLabel]) {
          grouped[parentLabel] = [];
        }
        grouped[parentLabel].push(item);
      });
      return grouped;
    } else {
      return {};
    }
  });
  </script>
  