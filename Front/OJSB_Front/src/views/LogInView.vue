<template>
  <div>

<!-- <form @submit.prevent="logIn">
   <div> -->
    <!-- <label for="username"> 아이디: </label>
    <input type="text" id="username" v-model.trim="username">

  </div>

  <label for="password"> 비밀번호: </label>
  <input type="password" id="password" v-model.trim="password"> -->
  <!-- <v-text-field
      label="아이디"
      type="text"
      v-model.trim="username"
      hide-details="auto"
      loading
    ></v-text-field>
    <v-text-field label="비밀번호" type="password" loading v-model.trim="password"></v-text-field>
  <v-btn variant="tonal">
    <input type="submit" value="로그인">
  </v-btn>
</form> -->
<!-- <v-sheet class="bg-deep-purple pa-12" rounded> -->
    <v-card class="mx-auto px-6 py-8 pt-10" max-width="344">
      <v-form
        v-model="form"
        @submit.prevent="logIn"
      >
        <v-text-field
          v-model.trim="username"
          :readonly="loading"
          :rules="[required]"
          class="mb-2"
          clearable
          label="Id"
        ></v-text-field>

        <v-text-field
          v-model="password"
          type="password"
          :readonly="loading"
          :rules="[required]"
          clearable
          label="Password"
          placeholder="Enter your password"
        ></v-text-field>

        <br>

        <v-btn
          :disabled="!form"
          :loading="loading"
          block
          color="success"
          size="large"
          type="submit"
          variant="elevated"
        >
          Sign In
        </v-btn>
      </v-form>
    </v-card>
  <!-- </v-sheet>  -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>

</style>