<template>
  
    <form ref="referenceRef" role="search" class="relative" @submit.prevent="submit">
      <div class="flex">
        <SfInput
          ref="inputRef"
          v-model="inputModel"
          wrapper-class="w-full !ring-0 active:!ring-0 hover:!ring-0 focus-within:!ring-0 border-y border-l border-neutral-200 rounded-r-none hover:border-primary-800 active:border-primary-700 active:border-y-2 active:border-l-2 focus-within:border-y-2 focus-within:border-l-2 focus-within:border-primary-700"
          aria-label="Search"
          placeholder="Search  Item Name"
          @focus="open"
          @keydown="handleInputKeyDown"
        >
          <template #prefix><SfIconSearch /></template>
          <template #suffix>
            <button
              v-if="inputModel"
              type="button"
              aria-label="Reset search"
              class="flex rounded-md focus-visible:outline focus-visible:outline-offset h-6 bg"
              @click="reset"
            >
              <SfIconCancel />
            </button>
          </template>
        </SfInput>
        <SfButton type="submit" square aria-label="Search for a specific phrase on the page" class="rounded-l-none">
          <SfIconSearch />
        </SfButton>
      </div>
      <div v-if="isOpen" ref="floatingRef" :style="style" class="left-0 right-0">
        <div
          v-if="isLoadingSnippets"
          class="flex items-center justify-center w-full h-screen sm:h-20 py-2 bg-white sm:border sm:border-solid sm:rounded-md sm:border-neutral-100 sm:drop-shadow-md"
        >
          <SfLoaderCircular />
        </div>
        <ul
          v-else-if="snippets.length > 0"
          ref="dropdownListRef"
          class="py-2 bg-white h-screen sm:h-auto sm:border sm:border-solid sm:rounded-md sm:border-neutral-100 sm:drop-shadow-md"
        >
          <li v-for="{ highlight, rest, product } in snippets" :key="product.item_name">
            <SfListItem
              tag="button"
              type="button"
              class="flex justify-start !py-4 sm:!py-2"
              @click="() => selectValue(product)"
              @keydown.enter.space.prevent="selectValue(product)"
            >
              <p class="text-left">
                <span>{{ highlight }}</span>
                <span class="font-medium">{{ rest }}</span>
              </p>
              <p class="text-left typography-text-xs text-neutral-500">{{ product.category }}</p>
            </SfListItem>
          </li>
        </ul>
      </div>
    </form>
  </template>
  
  <script lang="ts" setup>
  import { ref, watch } from 'vue';
  import { offset } from '@floating-ui/vue';
  import { watchDebounced } from '@vueuse/shared';
  import { unrefElement } from '@vueuse/core';
  import { createListResource, createResource } from 'frappe-ui';
  import { useRouter } from 'vue-router';
  
  import {
    SfButton,
    SfIconCancel,
    SfIconSearch,
    SfInput,
    SfListItem,
    SfLoaderCircular,
    useDisclosure,
    useDropdown,
    useTrapFocus,
  } from '@storefront-ui/vue';
  
  const inputModel = ref('');
  const inputRef = ref();
  const dropdownListRef = ref();
  const isLoadingSnippets = ref(false);
  const snippets = ref<{ highlight: string; rest: string; product: Product }[]>([]);
  const { isOpen, close, open } = useDisclosure();
  const { referenceRef, floatingRef, style } = useDropdown({
    isOpen,
    onClose: close,
    placement: 'bottom-start',
    middleware: [offset(4)],
  });
  const { focusables: focusableElements } = useTrapFocus(dropdownListRef as Ref<HTMLElement>, {
    trapTabs: false,
    arrowKeysUpDown: true,
    activeState: isOpen,
    initialFocus: false,
  });
  
  const router = useRouter();
  
  const submit = () => {
    close();
    alert(`Search for phrase: ${inputModel.value}`);
  };
  
  const focusInput = () => {
    const inputEl = unrefElement(inputRef)?.querySelector('input');
    inputEl?.focus();
  };
  
  const reset = () => {
    inputModel.value = '';
    snippets.value = [];
    close();
    focusInput();
  };
  
  const selectValue = (product: Product) => {
  inputModel.value = product.item_name; // Update input with selected product name
  snippets.value = [{
    highlight: '',
    rest: product.item_name,
    product,
  }];
  close(); // Close dropdown after selection
  // Navigate to product details page or perform other actions
  router.push({
    name: 'ProductDetailsPage',
    params: {
      id: product.item_name // Pass the item_code as the id
    }
  });
};

  
  
  const handleInputKeyDown = (event: KeyboardEvent) => {
    if (event.key === 'Escape') reset();
    if (event.key === 'ArrowUp') {
      open();
      if (isOpen && focusableElements.value.length > 0) {
        focusableElements.value[focusableElements.value.length - 1].focus();
      }
    }
    if (event.key === 'ArrowDown') {
      open();
      if (isOpen && focusableElements.value.length > 0) {
        focusableElements.value[0].focus();
      }
    }
  };
  
  watch(inputModel, () => {
    if (inputModel.value === '') {
      reset();
    }
  });
  
  watchDebounced(
    inputModel,
    () => { 
      const searchTerm = inputModel.value.trim();
      if (searchTerm) {
        const getSnippets = async () => {
          open();
          isLoadingSnippets.value = true;
          try {
            const data = await mockAutocompleteRequest(searchTerm);
            snippets.value = data;
          } catch (error) {
            close();
            console.error(error);
          }
          isLoadingSnippets.value = false;
        };
  
        getSnippets();
      } else {
        snippets.value = [];
        close();
      }
    },
    { debounce: 500 },
  );
  
  
  interface Product {
    id: string;
    name: string;
    category: string;
  }
  const products = createResource({
    url: 'ecommerce.api.get_products',
    auto: true,
  });
  
  const mockAutocompleteRequest = async (searchTerm: string): Promise<{ highlight: string; rest: string; product: Product }[]> => {
  if (products.data) {
    const results = products.data.filter(product => product.item_name.toLowerCase().includes(searchTerm.toLowerCase()));
    return results.map(product => {
      // Add a temporary ID
      product.id = product.item_code; // Or use another unique property
      const index = product.item_name.toLowerCase().indexOf(searchTerm.toLowerCase());
      const highlight = product.item_name.substring(0, index);
      const rest = product.item_name.substring(index, index + searchTerm.length);
      return {
        highlight,
        rest,
        product,
      };
    });
  } else {
    return [];
  }
};

  
  
  
  </script>