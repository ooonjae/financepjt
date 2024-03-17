<template>
  <div>
   <h2>회원정보 수정</h2>
   <form @submit="editUser" >
    

      <label for="nickname"> 이름 :</label>
      <input type="text" id="nickname" v-model.trim="nickname"><br>

      <label for="email"> 이메일 :</label>
      <input type="text" id="email" v-model.trim="email"><br>

      <label for="age"> 나이: </label>
      <input type="text" id="age" v-model.trim="age"><br>
      <!-- <p>숫자만 적어주세요</p> -->

      <label for="money"> 자산 : </label>
      <input type="text" id="money" v-model.trim="money"><br>

      <label for="salary"> 연봉 : </label>
      <input type="text" id="salary" v-model.trim="salary"><br>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter()
const store = useCounterStore()
const email = ref(null)
const nickname = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const myinfo = ref(null)
onMounted( () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/profile/`,
    headers:{
        Authorization: `Token ${store.token}`
      }
  })
  .then(res => {
    console.log(res.data)
    myinfo.value = res.data
    nickname.value = myinfo.value.nickname
    email.value = myinfo.value.email
    age.value = myinfo.value.age
    money.value = myinfo.value.money
    salary.value = myinfo.value.salary
    // router.push({name:'profile'})
  })
  .catch(err => console.log(err))
})

// const myinfo = store.profile

const editUser = function () {
  axios({
    method:'put',
    url: `${store.API_URL}/profile/`,
    data : {
      nickname: nickname.value,
      email: email.value,
      age : age.value,
      money: money.value,
      salary: salary.value
    },
    headers:{
        Authorization: `Token ${store.token}`
      }
  })
  .then(res =>{
    console.log(res.data)
    router.push({name:'profile'})
  })
  .catch(err => console.log(err))
}

</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
input{
  border-color: 1px solid black;
}
</style>