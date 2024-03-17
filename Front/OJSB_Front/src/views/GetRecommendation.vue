<template>
    <v-sheet  width="100%" class="pa-10 rounded-sm " v-if="isresult">

    <p class="text-h2 pa-10 text-center "> 당신에게 맞는 추천상품 </p>
    <v-card width="100%" v-for="item in items" class="ma-4 bg-indigo-lighten-3">
          <v-card-item>
            <v-card-title class="text-h6 ">{{ item.product.product.fin_prdt_nm }}</v-card-title>
            <hr>
            <v-card-title class="" style="color: white; font-weight: bold;">종합 점수 : {{ item.total }}</v-card-title>
            
          </v-card-item>
          <v-card-item>
            <v-expansion-panels v-for="reason in item.properties" class="bg-blue-grey-darken-1">
            <v-expansion-panel
                :title="reasons[reason]"
                :text="reason == 1? `${item.product.product.kor_co_nm} 이/가 주거래은행이에요`: item.product.product.spcl_cnd  "
            >
            </v-expansion-panel>
            </v-expansion-panels>

          </v-card-item>
          <v-card-text>
            얻을 수 있는 금액 확인해보기
          </v-card-text>
          <v-card-item class="justify-center">
            <v-btn class="text-h6 bg-light-blue-darken-2">
                상품 가입하러 가기
            </v-btn>
          </v-card-item>
    </v-card>


    </v-sheet>

    <v-divider></v-divider>
    <div class="text-center align-center flex-column" style="height: 100%; align-items: center; display: flex; flex-direction: column;" >
        <v-btn :disabled="dialog" :loading="dialog" color="purple-darken-2 ma-3" @click="dialog = true" size="x-large">
            Start loading
        </v-btn>
        <v-dialog v-model="dialog" :scrim="false" persistent width="auto">
            <v-card color="primary">
                <v-card-text>
                    추천 알고리즘 돌아가는 중
                    <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup>
import { watch, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import productComponent from '@/components/productComponent.vue';
import axios from 'axios';


const dialog = ref(false)
const isresult = ref(false)
const items = ref([])
const store = useCounterStore()
const reasons = ref(['','주거래 은행이에요', '첫 거래시 우대금리가 있어요', '고령자일시 추가금리가 있어요', '청년세대일시 추가금리가 있어요', '급여이체 통장으로 삼으면 추가금리가 있어요'])

const watcher = watch(dialog, (newthing, oldthing) => {
    if (oldthing == false){
    axios({
        url: `http://127.0.0.1:8000/profile/getRecommendation`,
        method: 'get',
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
        console.log(res)
        isresult.value = !isresult.value
        items.value = res.data
    })
        .catch((err) => {
        console.log(err)
    })
    setTimeout(() =>(
    dialog.value = false
    ), 1000)
    }
})
</script>

<style>
* {
    font-weight:bold;
}

</style>