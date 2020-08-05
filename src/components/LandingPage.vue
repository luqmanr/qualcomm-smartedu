<template>
    <div>

        <div class="container row">
            <img :src="logoITB" max-height="50%" width="50%" style="padding: 10%;">
            <div class="container col-md-12" style="font-weight: bolder;">Selamat Datang di SmartEdu App</div>
        </div>
        
    </div>
</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import logoITB from '../assets/logo-ITB.png'

export default {
    components: {

    },
    data() {
        return {
            logoITB: logoITB
        }
    },
    mounted() {
        axios.post(
            "http://localhost:3005/start_autotrain",
            {timeout: 1000}
        ).then(response => {
            console.log(response)
        }).catch(error => {
            console.log(error)
        })
    }
}

</script>

<style scoped>
    
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto;
    max-height: 90vh;
}

</style>