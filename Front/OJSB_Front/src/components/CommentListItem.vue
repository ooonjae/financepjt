<template>
  <div>
    <p> 익명 :  {{ comment.content }} 
    <button v-if="comment.user === store.profile.pk" @click="deleteComment">삭제</button>
    </p>
    <!-- <p>{{ comment }}</p> -->
  </div>
</template>

<script setup>
import axios from 'axios';
import { defineProps,onMounted,ref } from 'vue';
import { useCounterStore } from '@/stores/counter'

const props = defineProps({
  comment: Object
})

const store = useCounterStore()

onMounted( () => {
  store.getProfile()
})

const deleteComment = function () {
  axios({
    method: 'delete',
    url : `${store.API_URL}/api/comments/${props.comment.id}`
  })
  .then(res=> console.log(res.data))
  .catch(err=> console.log(err))
}

</script>

<style scoped>

</style>