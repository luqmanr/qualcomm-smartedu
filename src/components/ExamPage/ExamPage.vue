<template>

<div class="row">
    <b-overlay :show="overlay" opacity="0.0" style="max-width: 95vw; margin: 0 auto; padding: 10px;">

        <div id="user_formdata" class="container-fluid">

            <div class="row row-1" style="height: 90vh;">

                <div class="col-sm-4 col-md-4 col-xs-4 column-1" id="cheating_log">

                    <div style="height:0px;">
                        <cheating-log @emitCheatingData="receiveCheatingData" :monitoring-status="cheatingLogStatus"></cheating-log>
                    </div>     

                </div>

                <div class="col-sm-6 col-md-6 col-xs-6 column-2">

                    <!-- <p>{{examAnswers}}</p> -->
                    <div style="height:0px;">
                        <exam-questions @emitAnswers="receiveAnswers"></exam-questions>
                    </div>

                </div>

                <div class="col-sm-2 col-md-2 col-xs-2 column-3">

                    <div style="margin-left: -4vw; height: 40%; width: 100%;">
                        <webcam-stream :button-view="buttonView" style="transform: scale(0.8, 0.8);"></webcam-stream>
                    </div>
                    
                </div>

            </div>

        </div> 

        <!-- <b-overlay :show="overlay"> -->

        <template v-slot:overlay>
            <alert-modal 
              @emitOverlay="overlay=!overlay" 
              :alert-data="alertData"
              :button-class="buttonClass"></alert-modal>
        </template>
            
        <!-- </b-overlay> -->

    </b-overlay>

    <b-button variant="primary" @click="submitAnswers()" style="max-width: 95vw; margin: 0 auto; padding: 10px;" 
        class="col-md-12">Selesai!</b-button>

    <!-- <b-button variant="primary" @click="overlay=!overlay">
        Show overlay
    </b-button> -->
    <!-- <div>EXAM PAGE</div>
    <cheating-log></cheating-log>
    <webcam-stream></webcam-stream> -->
    <!-- <video src="https://www.w3schools.com/tags/movie.ogg" height="1080" width="1920"></video> -->
</div>

</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import CheatingLog from './CheatingLog.vue'
import ExamQuestions from './ExamQuestions.vue'
import WebcamStream from '../WebcamComponents/WebcamStreamCapture.vue'
import AlertModal from '../AlertComponents/AlertComponent.vue'

export default {
    components: {
        "cheating-log": CheatingLog,
        "exam-questions": ExamQuestions,
        "webcam-stream": WebcamStream,
        "alert-modal": AlertModal
    },
    data() {
        return {
            overlay: false,
            examAnswers: undefined,
            buttonView: false,
            cheatingData: undefined,
            alertData: undefined,
            cheatingMonitoringEndpoint: "http://localhost:3005/stop_monitoring",
            cheatingLogStatus: true,
            buttonClass: "danger"
        }
    },
    methods: {
        receiveAnswers(e) {
            this.examAnswers = e
            console.log(this.examAnswers)
        },
        submitAnswers() {
            this.stopCheatingMonitoring() // to stop cheating monitoring
            // this.startAutoTrain()

            const examAnswers = this.examAnswers
            var answers = []
            var i
            for (i in examAnswers) {
                answers.push(examAnswers[i])
            }

            // define JSON struct
            var userDataJSON = {
                "answers": answers
            };  
            // console.log(userDataJSON);
           

            // Endpoint location
            var apiEndpoint = this.registrationEndpoint
            // hit Endpoint with axios.post
            axios.post(apiEndpoint,
              JSON.stringify(userDataJSON),
              {headers :{'Content-Type': 'application/json'}},
              {timeout: 10})
            .then((response) => {
                // console.log(response)
                this.goToResultPage()
                // this.verifyStatus = true
                // this.goToExamPage()              
             }).catch(error => {
                console.log(error)
                // alert("PLEASE RETAKE YOUR PHOTO")
                })
            
            this.goToResultPage()
        },
        stopCheatingMonitoring() {
            axios.post(
                this.cheatingMonitoringEndpoint,
                {timeout: 1000})
              .then(response => {
                  console.log(response)
              }).catch(error => {
                  console.log(response)
              })
        },
        startAutoTrain() {
            axios.post(
                "http://localhost:3005/start_autotrain",
                {timeout: 3000}
              ).then(response => {
                  console.log(response)
              }).catch(error => {
                  console.log(error)
              })
        },
        receiveCheatingData(e) {
            // console.log("cheating data received")
            // console.log(e)
            this.cheatingData = e
            this.alertData = e[e.length -1][1]
            this.overlay = !this.overlay

            var container = this.$el.querySelector("#cheating_log");
            container.scrollTop = container.scrollHeight;
        },
        goToResultPage() {
            this.cheatingLogStatus = !this.cheatingLogStatus
            setTimeout(
                // this.$router.push("/"), 3000
                () => {
                    this.$router.push("/")
                }, 5000
            )
            // this.$router.go(this.$router.push("/"))
        }
    }
}
</script>

<style scoped>

.row-1 {
}

.column-1 {
    background-color: rgb(212, 212, 212);
    overflow-y: scroll;
    color: black;
}

.column-2 {
    background-color: rgb(212, 212, 212);
    overflow-y: scroll;
    color: black;
    font-weight: 500;
}

.column-3 {
    background-color: rgb(212, 212, 212);
    overflow: hidden;
    align-items: center;
    justify-content: center;
    color: black;
}

</style>
