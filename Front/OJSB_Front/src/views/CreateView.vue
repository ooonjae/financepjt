<template>
  <v-app>
    <v-app-bar app color="red" dark>
      <v-spacer></v-spacer>
      <v-app-bar-title>
        <div align="center" :style="{ fontSize: 'xx-large' }">게시판 {{$route.params.id}} 글쓰기</div>
      </v-app-bar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12" md="1">
            <v-btn color="cyan" @click="movetomain" :style="{ height: '50px', width: '90px', fontWeight: 'bold', fontSize: 'large' }">홈으로</v-btn>
          </v-col>
          <v-col cols="12" md="10">
            <v-card>
              <form @submit.prevent="createArticle">
                <v-text-field v-model.trim="title" dense outlined label="제목" style="width: 500px; margin-left: 100px;" :rules="[v => !!v || '제목은 필수입니다.']"></v-text-field>
                <v-textarea v-model.trim="content" label="내용" outlined rows="13" style="width: 730px; margin-left: 100px;"></v-textarea>
                <v-btn width="100px" style="margin-left: 600px; margin-bottom:30px;" @click="moveback">취소</v-btn>
                <v-btn width="100px" style="margin-left: 30px; margin-bottom:30px;" type="submit">제출</v-btn>
              </form>
            </v-card>
          </v-col>
          <v-col cols="12" md="1"/>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const router = useRouter();

const title = ref('');
const content = ref('');

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/articles/`,
    data : {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(()=>{
    router.push({name: 'article'})
  })
  .catch(err=>console.log(err))
}

const moveback = () => {
  router.back();
};

const movetomain = () => {
  router.push('/');
};
</script>

<!-- <template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목:</label>
      <input type="text" id="title" v-model.trim="title">

      <label for="content">내용:</label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <input type="submit" value="등록">


    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/articles/`,
    data : {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(()=>{
    router.push({name: 'article'})
  })
  .catch(err=>console.log(err))
}
</script>

<style scoped>

</style> -->