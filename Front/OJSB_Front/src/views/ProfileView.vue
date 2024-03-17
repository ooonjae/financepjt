<template>
  <div v-if="myinfo">
<h4 class="ma-10 pt-3">내프로필</h4><hr>
<div class="ma-10">
  <!-- <p>
    <strong>아이디: {{ myinfo.username }}</strong>
  </p>
  <p>
    <strong>이름:{{ myinfo.nickname }}</strong>
  </p>
  <p>
    <strong>이메일: {{ myinfo.email }}</strong>
  </p>
  <p>
    <strong>나이 : {{  myinfo.age }}</strong>
  </p>
  <p>
    <strong>자산 : {{  myinfo.money }} 원</strong>
  </p>
  <p>
    <strong>연봉: {{ myinfo.salary }} 원</strong>
  </p>
  <p>
    <strong>나의 가입 상품 목록 : {{ myinfo.financial_products }}</strong>
  </p>
  <p>
    <strong>상품 추천 목록</strong>
  </p> -->

  <v-card class="cardMaxWidth pa-3" max-width="100%" rounded="0">

      <v-container class="fill-height ">
        <v-row>
          <v-img
              class="pa-5 d-flex  justify-center align-center"
              height="100%"
              cover
              src="https://img.freepik.com/free-photo/white-paper-texture_1194-5998.jpg?size=626&ext=jpg&ga=GA1.1.569573680.1700638461&semt=ais"
            >
          <v-col cols="12" md="6" class="d-flex align-center justify-center">
            <v-avatar color="" size="150" rounded="0" ref="profileAvatar">
              <v-img
                cover
                class="rounded-image"
                src="https://i.namu.wiki/i/Bge3xnYd4kRe_IKbm2uqxlhQJij2SngwNssjpjaOyOqoRhQlNwLrR2ZiK-JWJ2b99RGcSxDaZ2UCI7fiv4IDDQ.webp"
              ></v-img>
            </v-avatar>
          </v-col>
        </v-img>
          
          <v-col cols="12" md="6">
            <v-tabs v-model="tab" background-color="transparent" centered >
              <!-- <v-tab v-for="(items, index) in tabs" :key="index">{{ items.title }}</v-tab> -->
              <v-tab>기본 정보</v-tab>
              <v-tab @click="Chartify">가입 상품</v-tab>
            </v-tabs>
            <!-- <v-divider></v-divider> -->

            <v-card-text>
              <v-window v-model="tab">
                <v-window-item :value="tabs[0].title">
                  <p><strong>{{ myinfo.user.nickname }}</strong>님의 프로필</p>
                  <v-divider></v-divider>
                  <p><strong>이메일 : {{ myinfo.user.email }}</strong></p>
                  <p><strong>나이 : {{ myinfo.user.age }}</strong></p>
                  <p><strong>자산 : {{ myinfo.user.money }}</strong></p>
                  <p><strong>급여 : {{ myinfo.user.salary }}</strong></p>
                  <v-divider></v-divider>
                </v-window-item>

                <v-window-item :value="tabs[1].title">
                  <p><strong>가입 상품 보기</strong></p>
                  <v-divider></v-divider>
                  <Bar
                id="my-chart-id"
                :options="chartOptions"
                :data="chartData"
                    />
                </v-window-item>

                <!-- <v-window-item :value="tabs[2].title">
                  Three
                </v-window-item> -->
              </v-window>
            </v-card-text>


          </v-col>
        </v-row>
      </v-container>
  </v-card>


  




</div>
  </div>
  <hr>
<RouterLink class="ml-3" :to="{name: 'profileedit'}">회원정보 수정</RouterLink>

</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import { onMounted, ref } from 'vue';
import Chart from 'chart.js/auto';
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
const store = useCounterStore()
const tabs = ref([
        { title: '기본 정보', subtitle: '부제목1', content: '나이, 자산, 연봉 등' },
        { title: '가입 상품', subtitle: '부제목2', content: '가입 상품 목록' },
])
const chartData = ref({
    labels: ['January', 'February', 'March'],
    datasets: []
})
const chartOptions = ref({
    responsive: true
})
const tab = ref(null)
onMounted( () => {
  store.getProfile()
  // console.log(store.profile)
  myinfo.value = store.profile
  // console.log(myinfo.value)
  // console.log('안녕하세요')
  // // const arasdf = myinfo.value.products.map((arg) => arg.fin_prdt_nm)
  // // chartData.value.labels = myinfo.value.products.map((arg) => arg.fin_prdt_nm)
  // // chartData.value.labels = myinfo.products.map((arg) => 
  // // {return arg.depositoptions_set ? arg.depositoptions_set[0].intr_rate : 0 }
  // // )
  // // console.log(myinfo.value.products.map((arg) => arg.fin_prdt_nm))

  // chartData.value.labels = myinfo.value.products.map((arg) => arg.fin_prdt_nm)
  // const arr1 = ref([])
  // const arr2 = ref([])
  // chartData.value.datasets = []
  // myinfo.value.products.forEach((arg) => {
  //   if (arg.depositoptions_set){
  //     arr1.value.push(arg.depositoptions_set[0].intr_rate)
  //     arr2.value.push(arg.depositoptions_set[0].intr_rate2)
  //   } else {
  //     arr1.value.push(0)
  //     arr2.value.push(0)
  //   }
 
  // })
  // console.log(chartData.value.labels)
  // console.log(arr1.value)
  // console.log(arr2.value)
  // chartData.value.datasets.push({ data : arr1.value})
  // chartData.value.datasets.push({ data : arr2.value})
})
const Chartify = function() {

  myinfo.value = store.profile
  console.log(myinfo.value)
  // const arasdf = myinfo.value.products.map((arg) => arg.fin_prdt_nm)
  // chartData.value.labels = myinfo.value.products.map((arg) => arg.fin_prdt_nm)
  // chartData.value.labels = myinfo.products.map((arg) => 
  // {return arg.depositoptions_set ? arg.depositoptions_set[0].intr_rate : 0 }
  // )
  // console.log(myinfo.value.products.map((arg) => arg.fin_prdt_nm))

  chartData.value.labels = myinfo.value.products.map((arg) => arg.fin_prdt_nm)
  const arr1 = ref([])
  const arr2 = ref([])
  chartData.value.datasets = []
  myinfo.value.products.forEach((arg) => {
    if (arg.depositoptions_set){
      arr1.value.push(arg.depositoptions_set[0].intr_rate)
      arr2.value.push(arg.depositoptions_set[0].intr_rate2)
    } else {
      arr1.value.push(0)
      arr2.value.push(0)
    }
 
  })
  console.log(chartData.value.labels)
  console.log(arr1.value)
  console.log(arr2.value)
  chartData.value.datasets.push({ data : arr1.value})
  chartData.value.datasets.push({ data : arr2.value})
}
const myinfo = ref(null)

// console.log(store.profile)
// console.log(myinfo.value)


</script>

<style scoped>
.rounded-image {
  border-radius: 50%;
}
.profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 선택적으로 카드의 최대 너비를 조절합니다. */
.cardMaxWidth {
  max-width: 100%;
}

</style>