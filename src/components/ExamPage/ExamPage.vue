<template>

<div class="row">
    <b-overlay :show="main_overlay" opacity="0.0" style="max-width: 95vw; margin: 0 auto; padding: 10px;">

        <div id="user_formdata" class="container-fluid" style="width: 100vw;">

            <div class="row row-1" style="height: 90vh;">

                <div class="col-sm-6 col-md-6 col-xs-6 column-1" id="cheating_log">

                    <div style="height:0px;">
                        <cheating-log @emitCheatingData="receiveCheatingData" :monitoring-status="cheatingLogStatus"></cheating-log>
                    </div>     

                </div>

                <!-- <div class="col-sm-6 col-md-6 col-xs-6 column-2">

                    <div style="height:0px;">
                        <exam-questions @emitAnswers="receiveAnswers"></exam-questions>
                    </div>

                </div> -->

                <b-overlay no-fade :show="col3_overlay" opacity="0.0" class="col-sm-6 col-md-6 col-xs-6 column-3">

                    <div style="height: 100%; width: 100%;">
                        <webcam-stream :button-view="buttonView" style="margin-top: 20vh; transform: scale(1.8, 1.8);"></webcam-stream>
                    </div>

                    <template v-slot:overlay>
                        <alert-modal 
                          @emitOverlay="col3_overlay=!col3_overlay" 
                          :alert-data="alertData"
                          button-variant=""
                          :button-class="col3ButtonClass"
                          style="margin-top: 45vh; margin-left: -10vw; width: 200%;"></alert-modal>
                    </template>
                    
                </b-overlay>

            </div>

        </div> 

        <!-- <template v-slot:overlay>
            <alert-modal 
              @emitOverlay="main_overlay=!main_overlay" 
              :alert-data="alertData"
              :button-class="mainButtonClass"></alert-modal>
        </template> -->
    

    </b-overlay>

    <b-button variant="primary" @click="submitAnswers()" style="max-width: 95vw; margin: 0 auto; padding: 10px;" 
        class="col-md-12">Selesai!</b-button>

    <!-- <b-button variant="primary" @click="col3_overlay=!col3_overlay">
        Show col3_overlay
    </b-button> -->

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
            main_overlay: false,
            col3_overlay: false,
            examAnswers: undefined,
            buttonView: false,
            cheatingData: undefined,
            alertData: undefined,
            cheatingMonitoringEndpoint: "http://localhost:3005/stop_monitoring",
            cheatingLogStatus: true,
            mainButtonClass: "danger",
            col3ButtonVariant: "primary",
            col3ButtonClass: "transparent"
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
            // alert(e[e.length -1][2])

            if (e[e.length -1][2] == "1") {
                this.col3ButtonClass = "transparent"
            } else if (e[e.length-1][2] == "2") {
                this.col3ButtonClass = "warning"
            } else {
                this.col3ButtonClass = "primary"
            }

            // this.main_overlay = !this.main_overlay
            this.col3_overlay = !this.col3_overlay

            var container = this.$el.querySelector("#cheating_log");
            container.scrollTop = container.scrollHeight;
        },
        goToResultPage() {
            this.cheatingLogStatus = !this.cheatingLogStatus
            setTimeout(
                // this.$router.push("/"), 3000
                () => {
                    this.$router.push("/")
                }, 10000
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
