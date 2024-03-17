<template>

      <th scope="row">{{ props.product.fin_prdt_cd }}</th>
        <td>{{ props.product.kor_co_nm }}</td>
        <td>{{ props.product.fin_prdt_nm }}</td>
        <td>{{ props.product.spcl_cnd }}</td>
        <td v-if="props.product.depositoptions_set">{{ props.product.intr_rate }}</td>
        <td v-if="props.product.depositoptions_set">{{ props.product.intr_rate2 }}</td>
        <td v-if="props.product.depositoptions_set">{{ props.product.save_trm }}</td>



</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
const props = defineProps({
    product : Object
})


</script>

<style  scoped>
.card{
    text-align: center;
    margin: 10px;
    display: inline-block;
}
*{
    background-color: inherit;
}
</style>