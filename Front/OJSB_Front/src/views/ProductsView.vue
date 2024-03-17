<template>
    <div>
            <!-- <Bar
                id="my-chart-id"
                :options="chartOptions"
                :data="chartData"
            /> -->
        <div class="container">

        <h2 style = "text-align: center; align-items: center;" id="itemComparison"><strong>상품 비교</strong></h2>
        <hr>

        <v-data-iterator :products="products" :page="page">
        <template v-slot:default="{ products }">
            <template
            v-for="(item, i) in products"
            :key="i"
            >
                        <v-card v-bind="item.raw"><p>하이</p></v-card>

                    <br>
            </template>
        </template>
        </v-data-iterator>

        
        <div class="card-container pd-5">         
            <div class="double-card">
                <span v-if="vs1 || vs2" class = "cardcontainerblock" >
                    <div class="row d-flex">
                            <v-card
                                class="mx-auto ma-2"
                                :max-width="calculateMaxWidth()"
                                height = "10rem"
                                :variant="variant"
                                v-if="vs1" @click="() => { vs1 = null }"
                            >
                        <v-card-item>
                            <div>
                                <h5 class="text-h6 mb-1">{{ vs1.fin_prdt_nm }}</h5>
                                <br>
                                <h6 class="text-overline mb-1">{{ vs1.etc_note }}</h6>
                                <!-- <p class="text-caption"></p> -->
                            </div>
                        </v-card-item>

                        </v-card>
                        <div class="col">
                        </div>

                          <v-card
                                class="mx-auto ma-2"
                                :max-width="calculateMaxWidth()"
                                height = "10rem"
                                :variant="variant"
                                v-if="vs2" @click="() => { vs2 = null }"
                            >
                            <v-card-item>
                                <div>
                                    <h5 class="text-h6 mb-1">{{ vs2.fin_prdt_nm }}</h5>
                                    <br>
                                    <h6 class="text-overline mb-1">{{ vs2.etc_note }}</h6>
                                    <!-- <p class="text-caption"></p> -->
                                </div>
                            </v-card-item>

                            </v-card>
                    </div>
                    <br>
                    <div class="row">
                        <v-btn type="button" class="btn btn-primary" @click="goDetail" v-if="vs1 && vs2"><p>상세히 비교하기</p></v-btn>
                        <v-btn type="button" class="btn btn-primary" @click="goDetail" v-else><p>상품 설명 보기</p></v-btn>
                    </div>

                </span>
                <span v-else class="cardcontainerblock">
                    <h1 style="color: #dee2e6; text-align: center;" ><strong >상품을 비교하기 위해선 선택을 해야합니다</strong></h1>
                </span>
            </div>
        </div>
        <hr>
        <h4 class="text-h4 text-center " id="location-search"><strong>상품 검색</strong></h4>

        <table class="table" id = "itemList">
        <thead>
            <tr>
            <th scope="col" >#</th>
            <th scope="col">은행</th>
            <th scope="col">상품 명</th>
            <th scope="col">우대 조건</th>
            <th scope="col" @click = "() => {
                asendesc[0] = -1 * asendesc[0]
                products.sort(function (a, b) { 
                    return (a.intr_rate - b.intr_rate) * asendesc[0]}
                    )}">
                금리
            </th>
            <th scope="col" @click = "() => {
                asendesc[1] = -1 * asendesc[1]
                console.log(asendesc[1])
                products.sort(function (a, b) { 
                    return (a.intr_rate2 - b.intr_rate2) * asendesc[1]}
                    )}">
                    우대금리</th>
            <th scope="col" @click = "() => {
                asendesc[2] = -1 * asendesc[2]
                products.sort(function (a, b) { 
                    return (a.save_trm - b.save_trm) * asendesc[2]}
                    )}">최대 투자 기간</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="product in products" @click="putup(product)"
            :class = "{ selected: vs1 && product.fin_prdt_nm == vs1.fin_prdt_nm, tableSecondary: vs1 && product.fin_prdt_nm == vs1.fin_prdt_nm }">
            <productComponent 
            :product = "product"/>
            </tr>
        </tbody>
        </table>
    </div>
    



    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import productComponent from '@/components/productComponent.vue';
import axios from 'axios';
import { useNavbarStore } from '@/stores/navbar';

import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
const navbar = useNavbarStore()
const sidebar = ref([
    {
        id : 'itemComparison',
        name: '상품 비교'
    },
    {
        id : 'itemList',
        name: '상품 목록'
    },
])
navbar.navBarList.value = sidebar.value
const page = ref(1)
const asendesc = ref([1, 1, 1, 1])
const router = useRouter()
const goDetail = function () {
    if(vs1.value && vs2.value){
        router.push({
            name: 'ProductsCompare', params: {
                ptcd1 : vs1.value.fin_prdt_cd,
                ptcd2 : vs2.value.fin_prdt_cd
            }
        })
    } else if (vs1.value) {
        console.log(vs1.value.fin_prdt_nm)
        router.push({
            name: 'ProductDetail', params : {
                ptcd1: vs1.value.fin_prdt_cd,
            }
        })
    } else if (vs2.value) {
        router.push({
            name: 'ProductDetail', params: {
                ptcd1: vs2.value.fin_prdt_cd,
            }
        })
    }
}
const products = ref([
        {
        'fin_prdt_cd' : 1,
        'kor_co_nm' : '아헿헿',
        'fin_prdt_nm' : '으헿', 
        'etc_note' : 'etc_note', 
        'join_deny' : 'join_deny', 
        'join_member' : 'join_member', 
        'join_way' : 'join_way', 
        'spcl_cnd' : 'spcl_cnd', 
        },
    ])

const vs1 = ref(null)
const vs2 = ref(null)
const isTrue = computed(() => {
    return vs1.value || vs2.value
})

onMounted(() => {
    axios({
        url: 'http://127.0.0.1:8000/api/finance/clientDepositProduct',
        method: 'get'
    })
        .then((res) => {
            products.value = res.data
            products.value.forEach((arg) => {
                let intr_rate = 0
                let intr_rate2 = 0
                let save_trm = 0
                arg.depositoptions_set.forEach((subarg) => {
                    if (subarg.intr_rate > intr_rate) { intr_rate = subarg.intr_rate }
                    if (subarg.intr_rate2 > intr_rate2) { intr_rate2 = subarg.intr_rate2 }
                    if (subarg.save_trm > save_trm) { save_trm = subarg.save_trm }
                })
                arg.intr_rate = intr_rate
                arg.intr_rate2 = intr_rate2
                arg.save_trm = save_trm
            }
            )        
        })
        .catch((err) => {
        console.log(err)
    })
})
const putup = (product) => {

    if (!vs1.value){
        vs1.value = product
    } else if(!vs2.value) {
        vs2.value = product
    } else {
        console.log('dd')
    }
}

const calculateMaxWidth = function() {
    // 하나의 카드만 선택된 경우 100%의 너비를 설정하고 두 개의 카드가 선택된 경우 각각 50%의 너비를 설정합니다.
    return vs1.value && vs2.value ? '45%' : '100%';
}

</script>

<style  scoped>

.card-container {
  display: flex;
  position: sticky; /* 스크롤 시 고정됨 */
  top: 0px; /* 화면 상단에 고정됨 */
  z-index: 100; /* 다른 요소 위에 표시 */
  width: 100%;
  background-color: white; 
  padding: 20px;
}
.cardcontainerblock {
    width: 100%;
    justify-content: center;
    align-items: center;
    background-color: white;
}
.row{
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
}

.card {
  display: flex;
  width: 45%;
  height: 200px;
  font-size: 1em;
  justify-content: center;
  flex-direction: column;
  background-color: #f0f8ff;
}

.double-card{
    display: flex;
    width: 100%;
    height: 100%;   
}
.selected{
    pointer-events: none;

}

.container {
    padding: 10px;
}
.table {
  /* 테이블의 스타일을 추가하세요 */
}
</style>