<template>
    <v-sheet 
    class="position-relative pa-10"
    min-height="450"
      >
      
    <v-dialog
    transition="dialog-bottom-transition"
    width="auto"
    >
    <template v-slot:activator="{props}">
    <p class ="text-h5 pa-5 font-weight-bold">제품 상세 설명</p>
    <hr>
    <span> <span class ="text-h5 pa-5 font-weight-bold">{{ options.fin_prdt_nm }}</span><span>{{ options.fin_prdt_cd}}</span></span>
    <p class="my-3"><span class=" text-h5 pa-5 ">{{ options.kor_co_nm }}</span></p>
    <v-container style="margin-left: 0;" class="">
        <v-row>
          <v-col>
            <v-card class = "bg-green-lighten-5">
              <v-card-title >이율 정보</v-card-title>
              <v-card-text>
                <v-row>
                  <v-col>
                    <v-list class = "bg-green-lighten-5">
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title class="text-h6">최고 이율</v-list-item-title>
                          <v-list-item-subtitle v-if="options.depositoptions_set">연 {{ options.depositoptions_set[0].intr_rate2 }}%</v-list-item-subtitle>
                          <v-list-item-subtitle v-else>해당 정보 없음</v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                  <v-col>
                    <v-list class = "bg-green-lighten-5">
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title class="text-h6">기본 이율</v-list-item-title>
                          <v-list-item-subtitle v-if="options.depositoptions_set">연 {{ options.depositoptions_set[0].intr_rate }}% ({{ options.depositoptions_set[0].save_trm }}개월, 세전)</v-list-item-subtitle>
                          <v-list-item-subtitle v-else>해당 정보 없음</v-list-item-subtitle>

                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-expansion-panels >
      <v-expansion-panel
        title="세부 조건 보기"
        class = "bg-green-lighten-4 mt-2"
        :text = "`가입 특약 : ${options.etc_note} 가입 조건 : ${options.spcl_cnd}` "
      >
      </v-expansion-panel>
        </v-expansion-panels>
        

        
        <v-btn width = 100% class="my-3" @click ="addList">상품 추가하기</v-btn>
      </v-container>


    
    <hr>
    <div class ="text-h5 pa-5 font-weight-bold">테이블로 보기</div>
      <v-table class="position-relative" >
        <thead>
            <tr>
            <th class="text-left" @click = "() => {
                asendesc[0] = -1 * asendesc[0]
                console.log(asendesc[0])
                options.depositoptions_set.sort(function (a, b) {
                    return (a.fin_prdt_cd - b.fin_prdt_cd) * asendesc[0]
                })}
                ">
              Name
            </th>
            <th class="text-left">
                금리 형태
            </th>
            <th class="text-left" @click = "() => {
                asendesc[1] = -1 * asendesc[1]
                console.log(asendesc[1])

                options.depositoptions_set.sort(function (a, b) {
                    return (a.save_trm - b.save_trm) * asendesc[1]
                })}">
              저축 기간
            </th>
            <th class="text-left" @click = "() => {
                asendesc[2] = -1 * asendesc[2]
                options.depositoptions_set.sort(function (a, b) { return (a.intr_rate - b.intr_rate)  * asendesc[2] })}">
              저축 금리
            </th>
            <th class="text-left"  @click = "() => {
                asendesc[3] *= -1
                options.depositoptions_set.sort(function (a, b) {
                    return (a.intr_rate2 - b.intr_rate2)  * asendesc[3]
            })}">
              최고 우대 금리
            </th>
        </tr>
        </thead>
        <tbody>
            <tr
            v-for="(option, index) in options.depositoptions_set"
            :key="index"
            v-bind="props"
            @click="putData(option)"
          >
          <td>{{ option.fin_prdt_cd }}</td>
          <td>{{ option.intr_rate_type_nm }}</td>
            <td>{{ option.save_trm  }}</td>
            <td>{{ option.intr_rate }}</td>
            <td>{{ option.intr_rate2 }}</td>
          </tr>
        </tbody>
    </v-table>
    </template>
    <template v-slot:default="{ isActive }">
    <v-card>
        <v-toolbar
            color="secondary"
            title="해당 상품의 투자 결과"
        ></v-toolbar>
        <v-card-text>
            <div class="text-h6 pa-12">최대 {{ Math.floor(chartData.datasets[1].data[chartData.datasets[0].data.length - 1]) }} 원을 모을 수 있어요</div>
            <Bar
                id="my-chart-id"
                :options="chartOptions"
                :data="chartData"
              />
        </v-card-text>
        <v-card-actions class="justify-end">
            <v-btn
            variant="text"
            @click="isActive.value = false"
            >Close</v-btn>
        </v-card-actions>
        </v-card>
    </template>
    </v-dialog>
</v-sheet>
    

</template>



<script setup>

import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import productComponent from '@/components/productComponent.vue';
import axios from 'axios';
import Chart from 'chart.js/auto';
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
const chartData = ref({
    labels: ['January', 'February', 'March'],
    datasets: []
})
const chartOptions = ref({
    responsive: true
})
const putData = function (option) {
    chartData.value.datasets = []
    const dat = [1000000]
    const dat2 = [1000000] 
    const label = []
    for (let i = 1; i < option.save_trm; i++){
        label.push(i)
        dat.push(dat[i - 1] * ( 1 + option.intr_rate / 100))
        dat2.push(dat2[i - 1] * ( 1 + option.intr_rate2 / 100))
    }
    console.log(dat)
    chartData.value.labels = label
    chartData.value.datasets.push({
        label : `${option.fin_prdt_cd} - 일반 금리`,
        data : dat
    })

    chartData.value.datasets.push({
        label: `${option.fin_prdt_cd} - 최고 우대 금리`,
        data: dat2
    })

}
const store = useCounterStore()
const addList = function () {
    axios({
        url: `http://127.0.0.1:8000/profile`,
        method: 'get',
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
            console.log(res.data, res.data.user.financial_products)
            if (res.data.user.financial_products == null) {
                console.log('없는것 취급')
                const params = { financial_products: options.value.fin_prdt_cd }
                axios({
                    url: `http://127.0.0.1:8000/profile/`,
                    method: 'put',
                    headers: {
                        Authorization: `Token ${store.token}`
                    },
                    data: {
                        financial_products: `${options.value.fin_prdt_cd}`
                    }
                })
            } else {
                const params = { financial_products: options.value.fin_prdt_cd }
                const sofar = res.data.user.financial_products.split(',')
                const k = sofar.findIndex((arg) => {
                    console.log(arg)
                    return arg == options.value.fin_prdt_cd
                })
                if (k != -1) {
                    console.log('있음')
                    // sofar.splice(k, 1)
                } else {
                  console.log('없음')  
                  sofar.push(options.value.fin_prdt_cd)
                    
                }
                const ok = sofar.join(',')
                console.log(sofar)
                console.log(ok)
                axios({
                    url: `http://127.0.0.1:8000/profile/`,
                    method: 'put',
                    headers: {
                        Authorization: `Token ${store.token}`
                    },
                    data: {
                        financial_products: ok ? ok : null
                    }
                })
            } 
        })
        .catch((err) => {
            console.log(err)
        })
}

const options = ref([])
const route = useRoute()
const asendesc = ref([1, 1, 1, 1])
onMounted(() => {
    const route = useRoute()
    console.log(route)
    axios({
        url: `http://127.0.0.1:8000/api/finance/clientDepositDetail/${route.params.ptcd1}`,
        method: 'get',
    })
        .then((res) => {
            console.log(res)
            options.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
})
</script>


<style scoped>
.row{
    position: absolute;
    display: flex;
}
</style>