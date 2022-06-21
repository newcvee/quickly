import { createRouter, createWebHistory } from 'vue-router'

const routes = [

  {
    path: '/',
    name: 'Orders history',
    component: () => import('@/pages/orders/OrdersHistoryPage.vue')
  },

  {
    path: '/clients-orders',
    name: 'Orders Description',
    component: () => import('@/pages/clients/OrdersDescriptionPage.vue')
  },

  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
