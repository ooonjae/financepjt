<template>
  <div>
    <!-- <h5>NO. {{ article.id }}</h5>
    <p>제목: {{ article.title }}</p>
    <RouterLink :to="{ name: 'detail', params: { id: article.id }}">
      <p>내용: {{ article.content }}</p>
    </RouterLink>
    <hr> -->
      <!-- <v-expansion-panels
      >
      
      
      <v-expansion-panel 
      :title="article.title"
      :text="article.content"  @click="router.push({name: 'detail', params: {id:article.id}})"
    class="ml-3 mb-3">
    </v-expansion-panel>
  </v-expansion-panels> -->
  </div>
          <v-row class="flex p-4 border-b border-b-gray-50" @click="router.push({name: 'detail', params: {id:article.id}})"  :class="{ 'elevation-5': hover }">
            <v-hover @mouseenter="isHovered = true" @mouseleave="isHovered = false">
            <v-col class="shrink-0">
              <v-avatar class="border border-orange-500 mr-4">
                <img
                  class="h-full object-cover"
                  loading="lazy"
                  src="https://lh3.googleusercontent.com/a/ALm5wu3tCZ0FQxd59NuRhNijQkQH5mrNe-37MH_KDz_q=s96-c"
                  alt="Profile Image"
                  width="60"
                  height="60"
                />
              </v-avatar>
              <v-divider
                class="ms-3"
                inset
                vertical
              ></v-divider>

              <v-divider
                class="ms-3"
                inset
                vertical
              ></v-divider>
              <v-text class="text-xl">[{{ props.article.title }}]</v-text>
            </v-col>
            <v-col>
              <v-text class="text-xl">{{ props.article.content.slice(0, 5) }}...</v-text>


            </v-col>

            <v-col class="flex grow-1 flex-col">
              <v-row class="flex items-center font-bold">
                <v-col>
                  <v-text class="text-xl">srcc01</v-text>
                </v-col>
              </v-row>
              <v-row class="font-medium color-gray-400 mt-1">Created at {{ props.article.created_at.slice(0,10) }}</v-row>
            </v-col>
          </v-hover>
          </v-row>
          <v-divider></v-divider>
</template>

<script setup>
import { RouterLink,useRouter } from 'vue-router'
import { ref } from 'vue'
const router = useRouter()
const isHovered = ref(false)
const props = defineProps({
  article: Object
})
console.log(props.article)
</script>
