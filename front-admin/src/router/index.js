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
    component: () => import('@/pages/categories/CategoriesPage.vue')
  },
  {
    path: '/add-category',
    name: 'Add Category',
    component: () => import('@/pages/categories/AddCategoryPage.vue')
  },

  {
    path: '/category/items/:category_id',
    name: 'Items',
    component: () => import('@/pages/items/ItemsPage.vue')
  },
  {
    path: '/add-item',
    name: 'Add Items',
    component: () => import('@/pages/items/AddItemsPage.vue')
  },
  {
    path: '/items/:id',
    name: 'OrdersCreate',
    component: () => import('@/pages/item-detail/ItemDetailPage.vue')
  },
  {
    path: '/Thanks',
    name: 'OrdersThanks',
    component: () => import('@/pages/item-detail/ThanksPage.vue')
  },
  {
    path: '/orders',
    name: 'OrdersCreate',
    component: () => import('@/pages/orders/OrdersHistoryPage.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
