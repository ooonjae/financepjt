import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import exchangeRate from '@/views/exchangeRate.vue';
import ProductsView from '@/views/ProductsView.vue';
import ProductDetail from '@/views/ProductsDetailView.vue';
import ProductsCompare from '@/views/ProductsCompare.vue';
import Mapview from '@/views/Mapview.vue';
import testingVuetify from '@/views/testingVuetify.vue';
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import EditView from '@/views/EditView.vue'
import ProfileView from '@/views/ProfileView.vue'
import EditProfileView from '@/views/EditProfileView.vue'
import HomeView from '@/views/HomeView.vue'
import GetRecommendation from '@/views/GetRecommendation.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/exchangeRate',
      name: 'exchangeRate',
      component: exchangeRate
    },
    {
      path: '/ProductsView',
      name: 'ProductsView',
      component: ProductsView
    },
    {
      path: '/Mapview',
      name: 'Mapview',
      component: Mapview
    },
    {
      path: '/ProductsCompare/:ptcd1/:ptcd2',
      name: 'ProductsCompare',
      component: ProductsCompare
    },
    {
      path: '/ProductDetailView/:ptcd1',
      name: 'ProductDetail',
      component: ProductDetail
    },
    {
      path: '/testingVuetify',
      name: 'testingVuetify',
      component: testingVuetify
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/articles',
      name: 'article',
      component: ArticleView
    },
    {
      path:'/articles/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path:'/article/create',
      name: 'articlecreate',
      component: CreateView
    },
    {
      path: '/article/:id/edit',
      name: 'articleedit',
      component: EditView
    },
    {
      path:'/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path:'/profile/edit',
      name: 'profileedit',
      component: EditProfileView
    },
    {
      path:'/GetRecommendation',
      name: 'GetRecommendation',
      component: GetRecommendation
    }
   
  ]
})

import { useCounterStore } from '@/stores/counter';

router.beforeEach((to,from)=>{
  const store = useCounterStore()
  if (to.name === 'article' && !store.isLogin){
    window.alert('로그인이 필요합니다')
    return { name: 'login'}
  }
  if ((to.name === 'SignUp' || to.name === 'login') && (store.isLogin)) {
    window.alert('로그인 상태 입니다.')
    return { name: 'ArticleView' }
  }
  
})

export default router
