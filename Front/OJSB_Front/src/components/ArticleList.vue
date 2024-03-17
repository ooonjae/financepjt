<template>
  <div>
    <h3 class="ml-3">글목록</h3><hr>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
    <!-- <v-list-item class="bg-white radius-md answer-card-box-shadow relative reply-row" tabindex="0">
      <v-container>
        <v-row class="flex p-4 border-b border-b-gray-50">
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
          </v-col>
          <v-col class="flex grow-1 flex-col">
            <v-row class="flex items-center font-bold">
              <v-col>
                <v-text class="text-xl">srcc01</v-text>
              </v-col>
            </v-row>
            <v-row class="font-medium color-gray-400 mt-1">Answered on February 12, 2017 12:09 PM</v-row>
          </v-col>
        </v-row>
        <v-row class="py-8 px-4 content-wrapper">
          <v-col>
            <v-row class="line-height-xl forumContent break-word" tabindex="0">
              <v-col>
                <v-text>
                  <p>
                    Hi &nbsp;- I am trying to add a simple bulletin board to my site that members can add items for
                    sale. Is there a widget or template that might be useful for this? I tried this widget to give you
                    the idea. If I use this widget, is there a way to save the entries? It would have been nice to have
                    a simple login for each person posting something so nobody else could edit or remove their post,
                    but that might be too complex for this particular widget.
                  </p>
                </v-text>
              </v-col>
            </v-row>
            <v-row class="mt-4 flex flex-col items-start">
              <v-col>
                <v-text class="font-bold locale">Page URL:</v-text>
              </v-col>
              <v-col>
                <v-link href="https://www.jotform.com/build/70424125478253" target="_blank" rel="nofollow ugc" class="color-blue-300 break-word">
                  https://www.jotform.com/build/70424125478253
                </v-link>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-list-item> -->
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
console.log(store.articles)
</script>

<style scoped>

</style>