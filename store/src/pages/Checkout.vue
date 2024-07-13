<template>
	<div>
		<h1>Checkout</h1>
         <pre>
			{{ cart.items }}
		</pre>

		<p v-if="cart.items.length === 0">Cart Empty</p>

		<Button v-else :loading="placeOrderResource.loading" @click="placeOrderResource.submit()">Place Order</Button>

		<ErrorMessage :message="placeOrderResource.error" />
	</div>
</template>

<script setup>
import {createResource, Button, ErrorMessage} from "frappe-ui";
import {inject} from "vue";

const cart = inject("cart");

const placeOrderResource = createResource({
	url: 'ecommerce.api.place_order',
	makeParams() {
		return {
			products: cart.items.map(item => ({
				item_name: item.product, // Assuming 'product' holds the item name
				qty: item.qty,
				image: item.image,
                item_code: item.item_code
			}))
		}
	}
})
</script>
