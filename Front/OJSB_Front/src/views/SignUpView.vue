<template>
  <div>
    
    <!-- <form @submit.prevent="signUp" >
      
      <label for="username"> 아이디  :</label>
      <input type="text" id="username" v-model.trim="username"><br>
      
     
      <label for="password1"> 비밀번호 :</label>
      <input type="password" id="password1" v-model.trim="password1"><br>
      
     
      <label for="password2"> 비밀번호 확인 :</label>
      <input type="password" id="password2" v-model.trim="password2"><br>

      <label for="nickname"> 이름 :</label>
      <input type="text" id="nickname" v-model.trim="nickname">

      <label for="email"> 이메일 :</label>
      <input type="text" id="email" v-model.trim="email">

      <label for="age"> 나이: </label>
      <input type="text" id="age" v-model.trim="age">
      

      <label for="money"> 자산 : </label>
      <input type="text" id="money" v-model.trim="money">

      <label for="salary"> 연봉 : </label>
      <input type="text" id="salary" v-model.trim="salary">

      <input type="submit">

    </form> -->

    <v-card
    class="mx-auto"
    max-width="500"
    title="회원가입"
    
  >
    <v-form v-model="form"  @submit.prevent="signUp">
      <v-text-field
      v-model.trim="username"
        color="primary"
        label="아이디"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model.trim="password1"
        type = 'password'
        color="primary"
        label="비밀번호"
        variant="underlined"
      ></v-text-field>

      <v-text-field
      v-model.trim="password2"
        type = 'password'
        color="primary"
        label="비밀번호 확인"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model.trim="nickname"
        color="primary"
        label="이름"
        
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model.trim="email"
        color="primary"
        label="이메일"
        
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model.trim="age"
        color="primary"
        label="나이"
        
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model.trim="money"
        color="primary"
        label="자산"
        
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model.trim="salary"
        color="primary"
        label="연봉"
        
        variant="underlined"
      ></v-text-field>

      
      <v-btn 
      color="success" 
      type="submit"
      :disabled="!form"
      :loading="loading"
      variant="elevated"
      >
        회원가입
  
        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-form>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

    </v-card-actions>
  </v-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()
console.log(store)
const username =ref(null)
const password1 =ref(null)
const password2 =ref(null)
const nickname =ref(null)
const email =ref(null)
const age =ref(null)

const money =ref(null)
const salary =ref(null)


const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    money: money.value,
    salary: salary.value
  }
  store.signUp(payload)
}
</script>

<style scoped>
form{
  display: flex;
  flex-direction: column;
}
</style>