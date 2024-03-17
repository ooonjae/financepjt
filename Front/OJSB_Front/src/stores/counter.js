import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const articles = ref([])
  const profile = ref(null)

  const getArticles = function (){
    axios({
      method: 'get',
      url: `${API_URL}/api/articles/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then( res => {
      console.log(res.data)
      articles.value = res.data
    })
    .catch( err => console.log(err))
  }
  
  const signUp = function (payload) {
    const { username, password1, password2, nickname, email, age, money, salary } = payload
  
    axios({
      method: 'post',
      url : `${API_URL}/accounts/signup/`,
      data: {
        username,
        email,
        password1,
        password2,
        nickname,
        age,
        
        money,
        salary,
       
      }
    })
      .then(res =>{
        console.log('회원가입 완료!')
        console.log(res.data)
        const password = password1
        logIn({username, password})
      })
      .catch(err => {
        console.log(err)
        console.log(err.data)}
         )
  
  }

  const logIn = function (payload) {
    const { username, password } =payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username, password
      }
    })
      .then( res => {
        console.log('로그인이 완료되었습니다.')
        console.log('res.data')
        token.value = res.data.key
        router.push({name: 'article'}) 
        // 잠시 게시판으로 이동
      })
      .catch( err => console.log(err))
  }
  const logout = function() {
    token.value = null
    console.log('로그아웃 되었습니다.')
    alert('로그아웃이 완료되었습니다.')
    router.push({name: 'home'})
  }

  const isLogin = computed(()=>{
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/profile/`, 
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        console.log('===========================')
        console.log(res.data)
        console.log('===========================')
        profile.value = res.data
      })
      .catch(err => console.log(err))
    }

  return { API_URL,token, signUp, logIn, articles, getArticles, isLogin, getProfile, profile, logout }
},{persist: true})
