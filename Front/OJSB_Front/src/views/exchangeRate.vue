<template>
    <div class="container mainbox shadow pt-3">
    <div class="container">
    <h3>환율 변경 페이지</h3>
    <div class="card preset--light">
        <div class="card-body tapestry-card-content">
            <div class="np-theme-personal">
                <div class="_ccConverter_f1zhf_1">
                    <div class="_ccCalculator_f1zhf_15">
                        <div class="form-group _ccSourceInput_f1zhf_10">
                            <label for="source-input" >금액</label>
                            <div class="input-group input-group-lg tw-money-input">
                                <input class="form-control np-form-control np-form-control--size-auto np-input np-input--shape-rectangle" id="source-input" inputmode="decimal" placeholder="" autocomplete="off" v-model = "currency1Value">
                                <form class="input-group-btn amount-currency-select-btn" >
                                    <div class="btn-group np-select btn-block">
                                        <select v-model="currency1" class="form-select form-select-lg btn btn-lg np-btn np-btn-lg btn-block np-btn-block np-dropdown-toggle  np-dropdown-toggle-navy dropdown-toggle" aria-label=".form-select-lg example">
                                            <option  v-for="rate in exchangeRates"  :value="rate"> {{ rate.cur_unit }}</option>
                                        </select>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="target-input">환전:</label>
                                <div class="tw-money-input input-group input-group-lg">
                                    <input class="form-control np-form-control np-form-control--size-auto np-input np-input--shape-rectangle" 
                                        id="target-input" 
                                        inputmode="decimal" 
                                        placeholder="" 
                                        autocomplete="off"
                                        :value="currencyFunction">
                                    <div class="input-group-btn amount-currency-select-btn">
                                        <div class="np-select btn-block btn-group">
                                           <form class="input-group-btn amount-currency-select-btn" >
                                        <div class="btn-group np-select btn-block">
                                            <select v-model="currency2" class="form-select form-select-lg btn btn-lg np-btn np-btn-lg btn-block np-btn-block np-dropdown-toggle  np-dropdown-toggle-navy dropdown-toggle" aria-label=".form-select-lg example">
                                                <option  v-for="rate in exchangeRates" :value="rate">{{ rate.cur_unit }}</option>
                                            </select>
                                        </div>
                                    </form>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="_ccCalculator_f1zhf_15">
                                <div class="text-xs-center text-lg-left">
                                    <h3 class="cc__source-to-target">
                                        <span class="dot-success animate-blink d-inline-block"></span>
                                        <span class="d-inline-block" v-if="currency1" > {{  currency1.cur_unit.indexOf('(100)') != -1 ? 100.000 : 1.00000}} {{ currency1.cur_unit }} = <span class="text-success" v-if="currency1 && currency2">{{ currency2.cur_unit.indexOf('(100)') != -1 ? currency1.deal_bas_r / currency2.deal_bas_r * 100  : currency1.deal_bas_r / currency2.deal_bas_r }} {{ currency2.cur_unit }}</span></span> 
                                    </h3>
                                    <div class="d-inline-flex align-items-center">
                                        <small class="m-r-1">Mid-market exchange rate at 06:59</small>
                                        <a href="https://wise.com/gb/mid-market-rate" 
                                        class="js-MidMarketLink text-no-decoration" 
                                        aria-label="기준 환율">
                                            <span class="tw-icon tw-icon-help-circle" aria-hidden="true" role="presentation">
                                                <svg width="16" height="16" fill="currentColor">
                                                    <path d="M9 11a1 1 0 11-2 0 1 1 0 012 0zM10.443 4.8A2.3 2.3 0 007.3 3.96L5.136 5.21l.8 1.385L8.1 5.345a.7.7 0 01.7 1.212l-2.165 1.25.8 1.386L9.6 7.943a2.3 2.3 0 00.842-3.142z"></path>
                                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M8 16A8 8 0 108 0a8 8 0 000 16zm0-1.6A6.4 6.4 0 108 1.6a6.4 6.4 0 000 12.8z"></path>
                                                </svg>
                                            </span>
                                        </a>
                                    </div>
                                </div>
                                <div class="_ccCalculator__cta_f1zhf_99" @click="expand = !expand">
                                    <a data-tracking-event="cc-calculator-track-rate-click" 
                                    class="btn btn--multi-row btn-accent btn-priority-2" 
                                    href="#rate-alerts">환율 추적
                                    </a>
                                </div>
                                <v-expand-transition>
                                <v-card
                                v-show="expand"
                                height="100%"
                                width="90%"
                                class="mx-auto justify-center"
                                >
                                <div v-if="currency2 && currency2.cur_unit != 'KRW'">
                                    <h4 class="text-center">{{ currency2.cur_nm }}의 현재 환율</h4>
                                    <img :src="`https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month3/FX_${currency2.cur_unit}KRW.png`" class=" align-self-center">
                                </div>
                                <div v-else>
                                    <div v-if="currency1">
                                    <h4 class="text-center">{{ currency1.cur_nm }}의 현재 환율</h4>

                                    <img :src="`https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month3/FX_${currency1.cur_unit}KRW.png`" class=" align-self-center">
                                    </div>
                                    <div v-else>
                                        <h2 class="text-center">추적할 데이터를 선택해주세요</h2>
                                    </div>
                                </div>
                                </v-card>
                                </v-expand-transition>
                            </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br>

    <h3>상세 환율 페이지</h3>

    <v-container>

        <!-- <v-btn v-bind="props" text="Open Dialog"> </v-btn> -->
        <v-row align="center" justify="center">
        <exchangeCard v-for="exchangeRate in exchangeRates"
        :currency = "exchangeRate"
        />
        </v-row>

    </v-container>
</div>
</div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import exchangeCard from '@/components/exchangeCard.vue';
import axios from 'axios';


const exchangeRates = ref([])
const currency1 = ref(null)
const currency2 = ref(null)
const currency1Value = ref(1000)
const currency2Value = ref(0)
const currencyFunction = computed(() => {
    if (currency1.value && currency2.value && currency1Value.value) {
        let currentValue = currency1Value.value
        if (currency1.value.cur_unit.indexOf('(100)') != -1) {
                currentValue /= 100
        }
        console.log(currentValue)
        return currency2.value.cur_unit.indexOf('(100)') != -1 ? currency1.value.deal_bas_r / currency2.value.deal_bas_r * 100 * currentValue : currency1.value.deal_bas_r / currency2.value.deal_bas_r * currentValue
    } else {
        return 0
    }
})
onMounted(() => {
    axios({
        url: 'http://127.0.0.1:8000/api/exchange/clientExchangeRate',
        method: 'get'
    })
        .then((res) => {
            exchangeRates.value = res.data
        console.log(exchangeRates.value)
        })
        .catch((err) => {
        console.log(err)
    })
})
const expand = ref(false)
const imageField = ref(false)

</script>

<style scoped>

</style>