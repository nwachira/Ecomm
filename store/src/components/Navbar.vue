<template>
  <header class="bg-gray-900 shadow-md transition-all duration-700 ease-in-out text-white sticky  top-0 z-50 mb-4" v-if="navitems.data">
    <nav class="flex justify-between items-center px-4 py-3 relative">
      <div class="flex items-center space-x-2">
        <Button theme="blue" variant="ghost" @click="toggleMenu">
          <FeatherIcon name="menu" class="h-6 w-6 text-white md:hidden" />
        </Button>
        <a href="/" class=" bg-white rounded-sm">
          <img :src="navitems.data.banner_image" alt="Logo" class="w-8 h-8 rounded-full object-cover" />
        </a>
        <h1 class="font-bold text-xl text-white hidden md:block">{{ navitems.data.brand_html}}</h1>
      </div>

      <div class="flex items-center space-x-4">
        <Button  size="lg" variant="solid" class="text-white" @click="dialog1 = true">
          <Badge size="sm">{{ cart.items.length }}</Badge>
          <FeatherIcon name="shopping-cart" class="h-6" />
        </Button>

        <template v-if="!session.isLoggedIn">
          <Button variant="outline" theme="blue" @click="login">
            <FeatherIcon name="user" class="h-6 w-6" />
          </Button>
        </template>

        <template v-else>
          <Dropdown
            :options="[
              {
                label: 'Profile',
                onClick: () => {},
              },
              {
                label: 'Settings',
                onClick: () => {},
              },
              {
                label: 'Logout',
                onClick: handleLogout, // Correct: Directly call the function
              },
            ]"
          >
            <Avatar
              shape="circle"
              :image="null"
              :label="session.user"
              size="lg"
              class="cursor-pointer h-8 w-8"
              variant="outline"
              theme="blue"
            />
          </Dropdown>
        </template>
      </div>
    </nav>

    <div class="mx-24 p-4">
      <TextInput
        type="search"
        size="lg"
        variant="subtle"
        placeholder="Search"
        :disabled="false"
        modelValue=""
        >
        <FeatherIcon name="search" class="h-6 w-6" />

    </TextInput>
    </div>

    <!-- Show Menu -->
    <ul class="flex-col md:flex-row md:items-center md:flex justify-center items-center px-6 py-3.5 bg-gray-900 duration-700 ease-in md:static absolute md:w-auto w-[80%] md:shadow-2xl mt-1 rounded-sm"
        :class="[open ? 'left-0' : 'left-[-100%]',]" >
      <li class="my-2 md:my-0 md:mx-4" v-for="item in navitems.data.top_bar_items" :key="item.name">
        <a :href="item.url" class="text-xl hover:text-amber-200">{{ item.label }}</a>
      </li>
    </ul>
  </header>

  <Dialog :options="{
		title: 'Your Cart',
		size: '3xl',
    
		actions: [
			{
				label: 'Proceed to checkout',
				variant: 'solid',
				onClick: (close) => {
					close();
					router.push({
						name: 'CheckoutPage'
					})

				}
			}
		]
	}" v-model="dialog1"
  :style="{ zIndex: 100 }"
	>
  <template #body-content>
    <ul class="space-y-4 mt-4">
      <li v-for="(item, index) in cartItems" :key="index">
        #{{ (index + 1) }} -
        <div class="flex items-center">
          <img :src="item.image" alt="" class="h-10 w-10 mr-2">
          <span>{{ item.product }}</span>
        </div>
        <div class="flex justify-center space-x-3">
          <h1>Qty</h1>
          <FormControl v-model="item.qty" type="number" placeholder="Qty" /> 
        </div>
        <Button @click="removeProductFromCart(index)" class="mt-2" variant="outline" theme="red">Remove</Button>
      </li>
    </ul>
  </template>
  
  
	</Dialog>
 
</template>

<script setup>
import { TextInput } from 'frappe-ui';
import { FeatherIcon } from 'frappe-ui';
import { Button, Avatar, Badge, Dialog, Dropdown, FormControl } from 'frappe-ui';
import { useRouter } from 'vue-router';
import { session } from '../data/session';
import { computed, ref, inject, watch } from 'vue';
import { createResource } from 'frappe-ui';

const router = useRouter();

const login = () => {
  router.push('/login');
};

const dialog1 = ref(false);
const open = ref(false);
const cart = inject("cart");
const toggleMenu = () => {
  open.value = !open.value;
};


const navitems = createResource({
  url: 'ecommerce.api.get_items',
  auto: true,
});

const handleLogout = async () => {
  await session.logout.submit(); // Wait for the logout to complete
  router.push('/'); // Redirect after logout
};


function removeProductFromCart(index) {
	cart.items.splice(index, 1);
}
const cartItems = ref(cart.items);

watch(cart.items, (newItems) => {
  cartItems.value = newItems;
});
</script>
