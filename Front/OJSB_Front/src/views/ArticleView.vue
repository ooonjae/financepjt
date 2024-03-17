<template>
   
    <v-container>
      <v-alert closable icon="$vuetify" text="댓글은 익명을 보장하며 자기가 쓴것만 지울 수 있습니다."></v-alert>
    </v-container>
  
<v-sheet  class ="pa-10">
  <div>
    <div
      class="px-10 bg-primary rounded"
    >
    <h1 class="text-h3 py-5 ">자유게시판</h1>
    </div>
<hr>
<v-btn>
<RouterLink id=make class='text-decoration-none text-button  text-center' :to="{name: 'articlecreate'}">글작성</RouterLink>
</v-btn>
  <hr>
<ArticleList/>
  </div>
</v-sheet>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { onMounted } from 'vue';
import {useCounterStore} from '@/stores/counter'
import { RouterLink } from 'vue-router';
const store = useCounterStore()

onMounted( () => {
  store.getArticles()
})


</script>



<style scoped>
h1{
  text-align: center;
}

</style>

