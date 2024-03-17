<template>
    <div>
        <h1>게시글 수정</h1>
        <!-- <p>{{ article.article }}</p> -->
    <form @submit.prevent="editArticle">
      <label for="title">제목:</label>
      <input type="text" id="title" v-model.trim="title">

      <label for="content">내용:</label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <input type="submit" value="수정">


     </form>
    </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter  } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
// import { RouterLink } from 'vue-router';


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const title = ref(null)
const content = ref(null)

onMounted( ()=>{
  axios({
    method: 'get',
    url: `${store.API_URL}/api/articles/${route.params.id}`
  })
  .then(res => {
    console.log(res.data)
    article.value = res.data
    console.log(article.value)
    title.value = article.value.article.title
    console.log(title.value)
    content.value = article.value.article.content
    console.log(content.value)
  })
  .catch(err => console.log(err))
})

const editArticle = function () {
    axios({
        method: 'put',
        url: `${store.API_URL}/api/articles/${route.params.id}/`,
        data : {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(()=>{
    router.push({ name: 'detail', params: { id: route.params.id }})
  })
  .catch(err=>console.log(err))
}


</script>

<style  scoped>

</style>