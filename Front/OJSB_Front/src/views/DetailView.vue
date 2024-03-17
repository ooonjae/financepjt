<template>
  <div class="pa-10">
    
    <div v-if="article">
      
      
      <!-- <h3 class="m-3">내용
      </h3><hr> -->
      <div class="m-3 pt-10" :height="2000">
          <h3 class="mb-10 font-weight-bold text-h3">
            {{ article.article.content }}
          </h3>
          
      </div><hr>
      
      <p class="ml-3">작성자 : {{ article.user }}</p>
      <hr>
      <div class="ml-3">

        <CommentList :article="article"/>
      </div>
      <hr>
      <div class="ml-3">

        <p>작성시간: {{ article.article.created_at.substr(0, 10) }} {{ article.article.created_at.substr(11,8) }}</p>
        <p>수정시간: {{ article.article.updated_at.substr(0, 10) }} {{ article.article.updated_at.substr(11, 8) }}</p>
      </div>
      
        <!-- <input type="text" v-model="commentContent">
        <button @click="createdComment">댓글 등록</button> -->
      <hr>
      <div class="ml-3" v-if="article.user===store.profile.user.username">
        <v-btn  prepend-icon="$vuetify">
          
          <RouterLink class='text-decoration-none' :to="{name: 'articleedit' }">수정</RouterLink>
        </v-btn>
        

        <v-btn class="bg-primary ml-3" @click="deleteArticle" prepend-icon="$vuetify">
  삭제
</v-btn>
        <!-- <button @click="deleteArticle">삭제</button> -->
      </div>
    </div>
  </div>
</template>


<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter  } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import CommentList from '@/components/CommentList.vue'


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
// const commentContent = ref(null)
// console.log(article.value.user)
// console.log(store.profile.username)
onMounted( ()=>{
  axios({
    method: 'get',
    url: `${store.API_URL}/api/articles/${route.params.id}`
  })
  .then(res => {
    console.log(res.data)
    article.value =  res.data
    store.getProfile()
    console.log(store.profile)
    console.log(store.profile.user)
  })
  .catch(err => console.log(err))
})

const deleteArticle = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/articles/${route.params.id}`
  })
    .then(res => {
      console.log(res.data)
      alert('글이 삭제 되었습니다.')
      router.push({name: 'article'})
    })
    .catch(err => console.log(err))
}

// const createdComment = function () {
//   axios({
//     method: 'post',
//     url: `${store.API_URL}/api/articles/${route.params.id}/comments/`,
//     data : {  
//       content: commentContent.value
//     },
//     headers: {
//       Authorization: `Token ${store.token}`
//     }
//   })
//   .then(res => {
//     console.log(res.data)
//   })
//   .catch(err => console.log(err))
// }

</script>

<style scoped>

</style>