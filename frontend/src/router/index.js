import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../pages/Home.vue')
    },
    {
      path: '/category',
      name: 'CategoryPage',
      component: () => import('../pages/CategoryPage.vue')
    },
    {
      path: '/:id',
      name: 'MovieDetail',
      component: () => import('../pages/movie-detail/MovieDetail.vue')
    }
  ]
})
