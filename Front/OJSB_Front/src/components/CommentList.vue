<template>
  <div>
    <h5>댓글 목록</h5>
    <div v-if="article.article.comment_count === 0">
      <p>댓글 이 없습니다.</p>
    </div>
    <div v-else>
      <CommentListItem v-for="comment in article.article.comment_set"
      :key="comment.id"
      :comment="comment"/>
    </div>

    <input type="text" v-model="commentContent" placeholder="댓글을 입력하세요">
    <button @click.prevent="createdComment">댓글 등록</button>
  </div>
</template>

<script setup>

import { ref, defineProps } from 'vue';
import { useRoute,useRouter } from 'vue-router';
import {useCounterStore} from '@/stores/counter'
import axios from 'axios';
import CommentListItem from '@/components/CommentListItem.vue';

const route =useRoute()
const router = useRouter()
const store = useCounterStore()
const props = defineProps({
  article: Object
})
const commentContent = ref(null)
// console.log(props.article.user)

const createdComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/articles/${route.params.id}/comments/`,
    data : {  
      content: commentContent.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    console.log(res.data)
    router.push({ name: 'detail', params: { id: route.params.id }})
  })
  .catch(err => console.log(err))
}

</script>

<style scoped>

</style>