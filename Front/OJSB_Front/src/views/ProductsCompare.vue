<template>

    <v-sheet class="position-relative pa-10" 
        min-height="450">
    <h1 class="font-weight-bold my-7 text-center">상품 비교</h1>

            <v-card>
                <h3 class="font-weight-bold my-5" >그래프로 확인</h3>
                <v-tabs v-model="tab" bg-color="primary">
                    <v-tab v-for ="item in set" :value="item" @click ="compareData(item)">{{ item }}개월</v-tab>
                </v-tabs>

                <v-card-text>
                    <v-window v-model="tab">
                        <v-window-item v-for ="item in set" :value="item">
                            <v-toolbar color="secondary" title="상품 투자 결과"></v-toolbar>
                            <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
                        </v-window-item>
                    </v-window>
                </v-card-text>
            </v-card>

        <v-dialog transition="dialog-bottom-transition" width="auto">
            <template v-slot:activator="{ props }">
                <h3 class="font-weight-bold my-5">상품 상세</h3>

                <v-table class="position-relative">
                    <thead>
                        <tr>
                            <th class="text-left" @click="() => {
                                asendesc[0] = -1 * asendesc[0]
                                console.log(asendesc[0])
                                options.sort(function (a, b) {
                                    return (a.fin_prdt_cd - b.fin_prdt_cd) * asendesc[0]
                                })
                            }
                            ">
                                Name
                            </th>
                            <th class="text-left">
                                금리 형태
                            </th>
                            <th class="text-left" @click="() => {
                                asendesc[1] = -1 * asendesc[1]
                                console.log(asendesc[1])

                                options.sort(function (a, b) {
                                    return (a.save_trm - b.save_trm) * asendesc[1]
                                })
                            }">
                                저축 기간
                            </th>
                            <th class="text-left" @click="() => {
                                asendesc[2] = -1 * asendesc[2]
                                options.sort(function (a, b) { return (a.intr_rate - b.intr_rate) * asendesc[2] })
                            }">
                                저축 금리
                            </th>
                            <th class="text-left" @click="() => {
                                asendesc[3] *= -1
                                options.sort(function (a, b) {
                                    return (a.intr_rate2 - b.intr_rate2) * asendesc[3]
                                })
                            }">
                                최고 우대 금리
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(option, index) in options" :key="index" v-bind="props" @click="putData(option)">
                            <td>{{ option.fin_prdt_cd }}</td>
                            <td>{{ option.intr_rate_type_nm }}</td>
                            <td>{{ option.save_trm }}</td>
                            <td>{{ option.intr_rate }}</td>
                            <td>{{ option.intr_rate2 }}</td>
                        </tr>
                    </tbody>
                </v-table>
            </template>
            <template v-slot:default="{ isActive }">
                <v-card>
                    <v-toolbar color="secondary" title="해당 상품의 투자 결과"></v-toolbar>
                    <v-card-text>
                        <div class="text-h6 pa-12">최대 {{
                            Math.floor(chartData.datasets[1].data[chartData.datasets[0].data.length - 1]) }} 원을 모을 수 있어요
                        </div>
                        <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
                    </v-card-text>
                    <v-card-actions class="justify-end">
                        <v-btn variant="text" @click="isActive.value = false">Close</v-btn>
                    </v-card-actions>
                </v-card>
            </template>
        </v-dialog>
    </v-sheet>
</template>



<script setup>

import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
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
const tab = ref(null)
const putData = function (option) {
    chartData.value.datasets = []
    const dat = [1000000]
    const dat2 = [1000000]
    const label = []
    console.log(option['intr_rate'])
    for (let i = 1; i < option.save_trm; i++) {
        label.push(i)
        dat.push(dat[i - 1] * (1 + option.intr_rate / 100))
        dat2.push(dat2[i - 1] * (1 + option.intr_rate2 / 100))
    }
    console.log(dat)
    chartData.value.labels = label
    chartData.value.datasets.push({
        label: `${option.fin_prdt_cd} - 일반 금리`,
        data: dat
    })

    chartData.value.datasets.push({
        label: `${option.fin_prdt_cd} - 최고 우대 금리`,
        data: dat2
    })
}
const compareData = function (trm) {
    console.log(trm)
    chartData.value.datasets = []
    const dat = [1000000]
    const dat2 = [1000000]
    const label = []
    for (let i = 1; i < trm; i++) {
        label.push(i)
        if (valueForChart.value[trm].vs1 != -1) {
            dat.push(dat[i - 1] * (1 + valueForChart.value[trm].vs1 / 100))
        }
        if (valueForChart.value[trm].vs2 != -1) {
            dat2.push(dat2[i - 1] * (1 + valueForChart.value[trm].vs2 / 100))
        }
    }
    chartData.value.labels = label
    if (valueForChart.value[trm].vs1 != -1) {
        chartData.value.datasets.push({
            label: `${options1.value[0].fin_prdt_cd}`,
            data: dat
        })
    }
    if (valueForChart.value[trm].vs2 != -1) {
        chartData.value.datasets.push({
            label: `${options2.value[0].fin_prdt_cd}`,
            data: dat2
        })
    }

}
const options = ref([])
const options1 = ref([])
const options2 = ref([])
const dialog = ref(false)

const valueForChart = ref({})
const route = useRoute()

const set = ref(new Set())
const ptcd1 = route.params.ptcd1
const ptcd2 = route.params.ptcd2
const asendesc = ref([1, 1, 1, 1])
onMounted(() => {
    const route = useRoute()
    console.log(route)
    axios({
        url: `http://127.0.0.1:8000/api/finance/clientDepositCompare/${route.params.ptcd1}/${route.params.ptcd2}`,
        method: 'get',
    })
        .then((res) => {
            options.value = res.data[ptcd1].concat(res.data[ptcd2])
            options1.value = res.data[ptcd1]
            options2.value = res.data[ptcd2]
            console.log(options1.value)

            for (const arg of options1.value) {
                set.value.add(arg.save_trm)
            }
            for (const arg of options2.value) {
                set.value.add(arg.save_trm)
            }
            console.log(options2.value)
            for (const arg of set.value) {
                console.log(arg)
                const tmp = {vs1 : -1, vs2 : -1}
                options1.value.forEach((val) => {
                    if (val.save_trm == arg) {
                        tmp.vs1 = Math.max(tmp.vs1, val.intr_rate)
                    }
                })
                options2.value.forEach((val) => {
                    if (val.save_trm == arg) {
                        tmp.vs2 = Math.max(tmp.vs2, val.intr_rate)
                    }
                })
                valueForChart.value[arg] = tmp
            }
            console.log(valueForChart.value)
        })
        .catch((err) => {
            console.log(err)
        })
})
</script>

<style scoped>
.row {
    position: absolute;
    display: flex;
}
</style>