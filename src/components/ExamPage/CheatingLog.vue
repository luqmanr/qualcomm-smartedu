<template>

<div style="height:100%;">
    <div style="font-weight: bolder;">CHEATING LOG</div>
    <div v-for="cheatingDataLines in cheatingData" class="row cheating_log" :class="statusCodeClass(cheatingDataLines[2])" style="font-size:small;">
        <div class="col-md-6">{{cheatingDataLines[0]}}</div>
        <div class="col-md-6">{{cheatingDataLines[1]}}</div>
        <!-- <div class="col-md-4">Status Code = {{cheatingDataLines[2]}}</div> -->
    </div>
    <!-- {{cheatingData}} -->
    <!-- <button @click="monitoringStatus = !monitoringStatus">Click</button> -->
</div>

</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { bus } from '../../main';

export default {
    props: {
        monitoringStatus: {
            default: false
        }
    },
    components: {

    },
    data() {
        return {
            cheatingData: [],
            cheatingLogIndex: 1,
            csvSkipTries: 3,
            // monitoringStatus: true
        }
    },
    methods: {
        fetchCSVIndex() {
            axios.get(
            'http://localhost:3005/cheating_log',
            { headers: { Pragma: 'no-cache'}, 
                timeout: 1000 })
            .then(response => {
                var csv_lines = response.data.split(/\r?\n/)
                if (csv_lines.length -1 > this.cheatingLogIndex) {
                    this.cheatingLogIndex = csv_lines.length - 2
                }
            }).catch(error => {
                console.log(error)
            })
        },
        fetchCheatingData() {
            this.fetchCSVIndex()
            setInterval(e => {       
                if (this.monitoringStatus == false) {
                    return
                }           
                axios.get(
                    'http://localhost:3005/cheating_log',
                    { headers: { Pragma: 'no-cache'}, 
                      timeout: 1000 })
                  .then(response => {
                        // console.log(response.data)
                        var csv_lines = response.data.split(/\r?\n/)
                        // if (csv_lines.length -1 > this.cheatingLogIndex) {
                        //     this.cheatingLogIndex = csv_lines.length - 2
                        // }
                        // console.log(csv_lines[1])
                        // this.cheatingLogIndex = (csv_lines.length) - 1
                        // console.log(this.cheatingLogIndex)
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
                // console.log("skipped")
                // return
                // this.skipCSVIndex()
            } else {
                // console.log("not skipped")
                // this.cheatingData.push(csv_lines[this.cheatingLogIndex])
                this.checkCheatingStatusCode(csv_lines)
                this.cheatingLogIndex ++
            }            
        },
        checkCheatingStatusCode(csv_lines) {
            var line = csv_lines[this.cheatingLogIndex].split(",")
            
            if (line[2] == "1") {
                // alert(line)
                // console.log(line[1], line[2])
                var timestamp = ((line[0].split("."))[0].split(" "))[1]
                var cheating_line = [timestamp, line[3], line[2]]
                this.cheatingData.push(cheating_line)
                this.emitCheatingdata()
                // console.log(cheating_line)
            } else if (line[2] == "2") {
                // console.log(line[1], line[2])
                var timestamp = ((line[0].split("."))[0].split(" "))[1]
                var cheating_line = [timestamp, line[3], line[2]]
                this.cheatingData.push(cheating_line)
                this.emitCheatingdata()
                // console.log(cheating_line)
            } else if (line[2] == "0") {
                var timestamp = ((line[0].split("."))[0].split(" "))[1]
                var cheating_line = [timestamp, line[3], line[2]]
                this.cheatingData.push(cheating_line)
                this.emitCheatingdata()
            }
            // else {
            //     this.csvSkipTries = this.csvSkipTries - 1

            //     if (this.csvSkipTries == 0 ){
            //         var timestamp = ((line[0].split("."))[0].split(" "))[1]
            //         var cheating_line = [timestamp, line[1], line[2]]
            //         this.cheatingData.push(cheating_line)
            //         this.emitCheatingdata()

            //         this.csvSkipTries = 3
            //     }
            //     // console.log(line[1], line[2])
            //     // return
            // }
        },
        statusCodeClass(statusCode) {
            if (statusCode == "1") {
                return "cheating"
            } else if (statusCode == "2") {
                return "warning"
            } else {
                return "normal"
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
        },
        changeStoppedStatus() {
            this.monitoringStatus = !this.monitoringStatus
        }
    },
    mounted() {
        // this.fetchCSVIndex()
        this.fetchCheatingData()
    }
}
</script>

<style scoped>

.cheating_log {
    overflow: hidden;
    align-items: center;
    justify-content: center;
    margin-top: 1vh;

    font-weight: 700;
    background-color: rgb(249, 255, 240);
} 
.cheating {
    background-color: rgb(255, 103, 103);
}
.warning {
    background-color: rgb(255, 115, 0);
}
.normal {
    background-color: rgb(119, 255, 153);
}

</style>
