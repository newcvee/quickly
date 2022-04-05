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
    path: '/category/dishes',
    name: 'Dishes',
    component: () => import('@/pages/orders-create/dishes/DishesPage.vue')
  },
  {
    path: '/dishes/:id',
    name: 'OrdersCreate',
    component: () => import('@/pages/orders-create/dish-detail/IngredientCounterPage.vue')
  },
  {
    path: '/Thanks',
    name: 'OrdersThanks',
    component: () => import('@/pages/orders-create/dish-detail/ThanksPage.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
