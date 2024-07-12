import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    name: 'Login',
    path: '/login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    name: 'ProductDetailsPage',
    path: '/product/:id',
    component: () => import('@/pages/ProductDetails.vue'),
  },
  {
    name: 'ProductPage',
    path: '/products',
    component: () => import('@/pages/ProductList.vue'),
  },

]

let router = createRouter({
  history: createWebHistory('/store'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }
  if(session.isGuest){
    router.replace({name:'Home'});
    return;
  }

  if (to.meta.requiresLogin && !isLoggedIn) {
    window.location.href='/login?redirect-to=/';
  } else {
    next()
  } 
  
})

export default router
