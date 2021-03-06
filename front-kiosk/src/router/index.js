import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/pages/about/AboutPage.vue'),
  },
  {
    path: '/categories',
    name: 'Categories',
    component: () => import('@/pages/orders-create/categories/CategoriesPage.vue')
  },
  {
    path: '/category/items/:category_id',
    name: 'Items',
    component: () => import('@/pages/orders-create/items/ItemsPage.vue')
  },

  {
    path: '/cart',
    name: 'Cart',
    component: () => import('@/pages/orders-create/cart/CartPage.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
