
import { tailwindConfig } from '@storefront-ui/vue/tailwind-config';

module.exports = {
  presets: [require('frappe-ui/src/utils/tailwind.config'), tailwindConfig],
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/@storefront-ui/vue/**/*.{js,mjs}'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
