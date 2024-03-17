<template>
  <v-dialog width="500">
      <template v-slot:activator="{ props }">
      <v-col
        cols="auto"
      >
      <v-card
        class="mx-auto"
        max-width="344"
        :variant="variant"
        v-bind="props"
      >
        <v-card-item>
          <div class="" style="width: 10rem;">
              <h5 class="text-overline mb-1">{{ Props.currency.cur_nm }}</h5>
              <h6 class="text-h6">{{ Props.currency.cur_unit }}</h6>
              <!-- <p class="text-caption"></p> -->
          </div>
        </v-card-item>
        <v-card-actions>
          <v-btn
          :href = " Props.currency.cur_unit.indexOf('(100)') == -1? `https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_${Props.currency.cur_unit}KRW` : `https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_${Props.currency.cur_unit.slice(0, -5)}KRW`">
            상세 조회
          </v-btn>
        </v-card-actions>
      </v-card>
      </v-col>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card title="환율 차트">
          <v-card-text>
            {{ Props.currency.cur_nm }}
          </v-card-text>
          <img :src="Props.currency.cur_unit.indexOf('(100)') == -1 ? `https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month3/FX_${Props.currency.cur_unit}KRW.png` : `https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month3/FX_${Props.currency.cur_unit.slice(0, -5)}KRW.png`" alt="">

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn text="Close Dialog" @click="isActive.value = false"></v-btn>
          </v-card-actions>
        </v-card>
      </template>
  </v-dialog>
  
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
const Props = defineProps({
    currency : Object
})
console.log(Props.currency)


</script>

<style scoped>
.card{
    text-align: center;
    margin: 10px;
    display: inline-block;
}
</style>

