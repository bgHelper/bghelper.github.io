const routes = [
  {
    path: '/',
    name : 'Indxe',
    component: () => import('pages/Index.vue')
  },
  {
    path: '/List',
    name: 'List',
    component: () => import('pages/List.vue')
  },
  {
    path: '/Hall',
    name: 'Hall',
    component: () => import('pages/Hall.vue')
  },
  {
    path: '/About',
    name : 'About',
    component: () => import('pages/About.vue')
  },
  {
    path: '/Error404',
    name : 'Error404',
    component: () => import('pages/Error404.vue')
  },
  {
    path: '/:gid(\\d+)/Rule',
    name : 'Rule',
    component: () => import('src/pages/Rule.vue'),
    meta: () => import('assets/gameList.js')
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    redirect: { 
      name : 'Error404'
    }
  },
]

export default routes
