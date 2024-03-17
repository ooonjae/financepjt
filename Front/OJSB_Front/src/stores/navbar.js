import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useNavbarStore = defineStore('navbar', () => {
    const router = useRouter()
    const navBarList = ref([])
    const changeNavBar = function () {
        
    }
  
  return { navBarList }
}, { persist: true })



