<template>
    <v-app id="inspire">
      <v-app-bar flat>
          <v-container class="mx-auto d-flex align-center justify-center">
          <v-avatar
          class="me-4 "
          color="grey-darken-1"
          size="32"
          ></v-avatar>
          <v-app-bar-title>
            

                OJSB
            
            </v-app-bar-title>
            

              <!-- <v-btn
                v-for="link in links"
                :key="link.id"
                :text="link.name"
                @click = "() => {
                  router.push({name : link.id })
                }"
                variant="text"
              ></v-btn> -->
         
              <v-btn>
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'home'}">Home</RouterLink>
              </v-btn>
              <v-btn>
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'exchangeRate'}">환율 서비스</RouterLink>
              </v-btn>
              <v-btn>
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'ProductsView'}">제품 비교 서비스</RouterLink>
              </v-btn>
              <v-btn>
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'Mapview'}">지도 서비스</RouterLink>
              </v-btn>
              <v-btn>
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'article'}">자유게시판</RouterLink>
              </v-btn>
              <v-btn v-if="store.isLogin">
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'profile'}">내프로필</RouterLink>
              </v-btn>
              <v-btn>
                <RouterLink class='text-decoration-none text-color-black' :to="{name: 'GetRecommendation'}">금융상품 추천받기</RouterLink>
              </v-btn>
              <p class="ml-13"></p>
              
                  <v-btn v-if="!store.isLogin" class="ml-13">
                    <RouterLink class='text-decoration-none text-color-black' :to="{name: 'SignUp'}">회원가입</RouterLink>
                  </v-btn>
                  
                  <v-btn v-if="!store.isLogin">
                    <RouterLink class='text-decoration-none text-color-black' :to="{name: 'login'}">로그인</RouterLink>
                  </v-btn>
              
              <div v-if="store.isLogin" class="ml-13">
                <v-btn @click="logout">
                    로그아웃
                </v-btn>
              </div>
              

  
          <v-spacer></v-spacer>
  
        
        </v-container>
      </v-app-bar>
  
      <v-main class="bg-grey-lighten-3">
        <v-container class="d-flex align-center " >
          <v-row>
            <!-- <v-col cols="2">
              <v-sheet rounded="lg">
                <v-list rounded="lg">
                  <v-list-item
                    v-for="n in sidebar"
                    :key="name"
                    :href = "`#${n.id}`"
                    :title="n.name"
                  ></v-list-item>
  
                  <v-divider class="my-2"></v-divider>
  
                  <v-list-item
                    color="grey-lighten-4"
                    link
                    title="Refresh"
                  ></v-list-item>
                </v-list>
              </v-sheet>
            </v-col> -->
  
            <v-col>
              <v-sheet 
                min-height="70vh"
                class="mx-auto"
                :rounded="xl"
                :elevation="24" :height="2000" :width="1800"
              >
                <RouterView />
 
  

              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import { useNavbarStore } from '@/stores/navbar';
  import { RouterLink } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  
  const store = useCounterStore()
  
 const logout = function () {
    store.logout()
 }

  const links = ref([
    {
        name: 'Home',
        id: 'home'
    },
    
    {
        name: '환율 서비스',
        id: 'exchangeRate'
    },
    {
        name: '제품 비교 서비스',
        id: 'ProductsView'
    },
    {
        name: '지도 서비스',
        id: 'Mapview'
    },
    
    {
        name: '자유게시판',
        id: 'article'
    },
    {
        name: '내프로필',
        id: 'profile'
    },
    {
        name: '회원가입',
        id: 'SignUp'
    },
    {
        name: '로그인',
        id: 'login'
    },
  
  ])
  
  const navbar = useNavbarStore()
  // const sidebar = ref(navbar.navBarList.value)
  const sidebar = computed(() => {
    return navbar.navBarList.value
  })
  
  
  //            <p>
  // < RouterLink : to = "{ name: 'SignUp'}" > SignUp</RouterLink>|
  //   <RouterLink: to="{name: 'login'}" > 로그인</RouterLink: >
  //     <RouterLink: to="{ name: 'exchangeRate' }" > rate</RouterLink: > |
  //       <RouterLink: to="{ name: 'ProductsView' }" > products</RouterLink: > |
  //         <RouterLink: to="{ name: 'Mapview' }" > Mapview</RouterLink: > |
  //           <RouterLink: to="{ name: 'testingVuetify' }" > testingVuetify</RouterLink: > |
  //           </p >
  const router = useRouter()
  
  </script>
  
  <style>
  a {
    color: black;
  }
  </style>
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
