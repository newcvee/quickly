import { createRouter, createWebHistory } from 'vue-router'

const routes = [

  {
    path: '/orders-history',
    name: 'Orders history',
    component: () => import('@/pages/orders/OrdersHistoryPage.vue')
  },

  {
    path: '/order-description',
    name: 'Orders Description',
    component: () => import('@/pages/order-description/OrdersDescriptionPage.vue')
  },

  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
