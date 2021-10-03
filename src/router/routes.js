import gameData from '../assets/gameList'

const routes = [
  {
    path: '/',
    name : "Indxe",
    component: () => import('pages/Index.vue')
  },
  {
    path: '/List',
    name: "List",
    component: () => import('pages/List.vue')
  },
  {
    path: '/Hall',
    name: "Hall",
    component: () => import('pages/Hall.vue')
  },
  {
    path: '/About',
    component: () => import('pages/About.vue')
  },
  {
    path: '/:gid',
    component: () => import('pages/Empty.vue'),
    //beforeEnter: (to, from, next) => {
    //  // ...
    //  console.log(to)
    //  if (to.params.gid == "822") {
    //    console.log("matched")
    //    next({name : "404"})
    //    return
    //  }
    //  next()
    //},
    children: [
      { 
        path: '',
        redirect : "Rule"
      },
      { 
        path: 'Rule',
        name: "Rule",        
        component: () => import('pages/Rule.vue')
      }
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    name : "404",
    component: () => import('pages/Error404.vue')
  }
]

export default routes
