<template>
    <v-app id="inspire">
      <v-app-bar flat>
        
        <v-container class="mx-auto d-flex align-center justify-center">
          <v-avatar
            class="me-4 "
            color="grey-darken-1"
            size="32"
          ></v-avatar>
          <v-app-bar-title>OJSB</v-app-bar-title>
          <v-btn
            v-for="link in links"
            :key="link.id"
            :text="link.name"
            @click = "() => {
              router.push({name : link.id })
            }"
            variant="text"
          ></v-btn>
  
          <v-spacer></v-spacer>
  
          <v-responsive max-width="160">
            <v-text-field
              density="compact"
              flat
              hide-details
              label="Search"
              rounded="lg"
              single-line
              variant="solo-filled"
            ></v-text-field>
          </v-responsive>
        </v-container>
      </v-app-bar>
  
      <v-main class="bg-grey-lighten-3">
        <v-container>
          <v-row>
            <v-col cols="2">
              <v-sheet rounded="lg">
                <v-list rounded="lg">
                  <v-list-item
                    v-for="n in 5"
                    :key="n"
                    link
                    :title="`List Item ${n}`"
                  ></v-list-item>
  
                  <v-divider class="my-2"></v-divider>
  
                  <v-list-item
                    color="grey-lighten-4"
                    link
                    title="Refresh"
                  ></v-list-item>
                </v-list>
              </v-sheet>
            </v-col>
  
            <v-col>
              <v-sheet
                min-height="70vh"
                rounded="lg"
              >
                <!--  -->
              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script setup>
  import {ref, onMounted} from 'vue';
  import { useRouter } from 'vue-router';
  
    const links = ref([
        {
        name: '회원가입',
        id : 'SignUp'
        },
        {
        name: '로그인',
        id : 'login'
        },
        {
        name: '환율 서비스',
        id : 'exchangeRate'
        },
        {
        name: '제품 비교 서비스',
        id : 'ProductsView'
        },
        {
        name: '제품 비교 서비스',
        id : 'ProductsView'
        },
        {
        name: '지도 서비스',
        id : 'Mapview'
        },

    ])
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
  
