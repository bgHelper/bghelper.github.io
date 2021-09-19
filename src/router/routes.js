
const routes = [
  {
    path: '/',
    component: () => import('pages/Index.vue')
  },
  {
    path: '/List',
    component: () => import('pages/List.vue')
  },
  {
    path: '/Hall',
    component: () => import('pages/Hall.vue')
  },
  {
    path: '/About',
    component: () => import('pages/About.vue')
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
