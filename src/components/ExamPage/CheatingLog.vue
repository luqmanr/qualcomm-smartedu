<template>

<div style="height:100%;"">
    <div>CHEATING LOG</div>
    <div v-for="cheatingDataLines in cheatingData" class="row" style="font-size:small;">
        <div class="col-md-4">Timestamp = {{cheatingDataLines[0]}}</div>
        <div class="col-md-4">Message = {{cheatingDataLines[1]}}</div>
        <div class="col-md-4">Status Code = {{cheatingDataLines[2]}}</div>
    </div>
    <!-- {{cheatingData}} -->
</div>

</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { bus } from '../../main';

export default {
    components: {

    },
    data() {
        return {
            cheatingData: [],
            cheatingLogIndex: 1,
            csvSkipTries: 3
        }
    },
    methods: {
        fetchCheatingData() {
            setInterval(e => {                    
                axios.get(
                    'http://localhost:3005/cheating_log',
                    { headers: { Pragma: 'no-cache'}, 
                      timeout: 1000 })
                  .then(response => {
                        // console.log(response.data)
                        var csv_lines = response.data.split(/\r?\n/)
                        this.cheatingLogUpdate(csv_lines)
                        // this.emitCheatingdata()
                  }).catch(error => {
                        console.log(error)
                        // this.cheatingData.push("YOU ARE NOT CHEATING")
                        // this.emitCheatingdata()
                    })
            }, 50)
        },
        cheatingLogUpdate(csv_lines) {
            // console.log(csv_lines)
            if (csv_lines[this.cheatingLogIndex] == "" || csv_lines[this.cheatingLogIndex] == null) {
                console.log("skipped")
                // this.skipCSVIndex()
            } else {
                console.log("not skipped")
                // this.cheatingData.push(csv_lines[this.cheatingLogIndex])
                this.checkCheatingStatusCode(csv_lines)
                this.cheatingLogIndex ++
            }            
        },
        checkCheatingStatusCode(csv_lines) {
            var line = csv_lines[this.cheatingLogIndex].split(",")
            if (line[2] == "1") {
                // alert(line)
                console.log(line[1], line[2])
                this.cheatingData.push(line)
                this.emitCheatingdata()
            } else {
                console.log(line[1], line[2])
            }
        },
        skipCSVIndex() { // enable this function if you want to skip a row in the csv file
            this.csvSkipTries = this.csvSkipTries - 1
            if (this.csvSkipTries <= 0) {
                this.cheatingLogIndex ++
                this.csvSkipTries = 3
            }
        },
        emitCheatingdata() {
            this.$emit("emitCheatingData", this.cheatingData)
        }
    },
    mounted() {
        this.fetchCheatingData()
    }
}
</script>

<style scoped>

</style>
