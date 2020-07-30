<template>

<div style="height:100%;"">
    <div>CHEATING LOG</div>
    {{cheatingData}}
</div>

</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

export default {
    components: {

    },
    data() {
        return {
            cheatingData: []
        }
    },
    methods: {
        fetchCheatingData() {
            setInterval(e => {                    
                axios.get(
                    'https://locahost:89239',
                    { timeout: 3000 })
                  .then(response => {
                        console.log(response)
                        this.cheatingData.push("YOU ARE CHEATING")
                  }).catch(error => {
                        console.log(error)
                        this.cheatingData.push("YOU ARE NOT CHEATING")
                    })
            }, 1000)
        }
    },
    mounted() {
        this.fetchCheatingData()
    }
}
</script>

<style scoped>

</style>
