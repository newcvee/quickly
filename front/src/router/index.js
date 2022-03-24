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
    path: '/orders-create',
    name: 'OrdersCreate',
    component: () => import('@/pages/orders-create/dish-detail/IngredientsComponent.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
