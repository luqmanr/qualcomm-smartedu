<template>

<div>
    <b-overlay :show="overlay" opacity="0.0" style="max-width: 95vw; margin: 0 auto; padding: 10px;">

        <div id="user_formdata" class="container-fluid">

            <div class="row row-1" style="height: 90vh;">

                <div class="col-sm-3 col-md-3 col-xs-3 column-1" >
                    COLUMN 1
                    <div style="height:0px;">
                        <cheating-log @emitCheatingData="receiveCheatingData"></cheating-log>
                    </div>                    
                </div>

                <div class="col-sm-6 col-md-6 col-xs-6 column-2">
                    COLUMN 2
                    <p>{{examAnswers}}</p>
                    <div style="height:0px;">
                        <exam-questions @emitAnswers="receiveAnswers"></exam-questions>
                    </div>
                </div>

                <div class="col-sm-3 col-md-3 col-xs-3 column-3">
                    COLUMN 3
                    <div style="margin: auto; overflow: hidden; height: 40%; width: 100%;">
                        <webcam-stream :button-view="buttonView"></webcam-stream>
                    </div>
                </div>

            </div>

        </div> 

        <!-- <b-overlay :show="overlay"> -->

            <template v-slot:overlay>
                <alert-modal @emitOverlay="overlay=!overlay" :alert-data="alertData"></alert-modal>
            </template>
            
        <!-- </b-overlay> -->

    </b-overlay>

    <b-button variant="primary" @click="overlay=!overlay">
        Show overlay
    </b-button>
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
        }
    },
    methods: {
        receiveAnswers(e) {
            this.examAnswers = e
            console.log(this.examAnswers)
            this.submitAnswers()
        },
        submitAnswers() {
            const examAnswers = this.examAnswers
            var answers = []
            var i
            for (i in examAnswers) {
                answers.push(examAnswers[i])
            }

            // define JSON struct
            var userDataJSON = {
                "answers": answers
            };  console.log(userDataJSON);
           

            // Endpoint location
            var apiEndpoint = this.registrationEndpoint
            // hit Endpoint with axios.post
            axios.post(apiEndpoint,
              JSON.stringify(userDataJSON),
              {headers :{'Content-Type': 'application/json'}},
              {timeout: 10})
            .then((response) => {
                console.log(response)
                // this.verifyStatus = true
                // this.goToExamPage()              
             }).catch(error => {
                console.log(error)
                // alert("PLEASE RETAKE YOUR PHOTO")
                })
        },
        receiveCheatingData(e) {
            console.log("cheating data received")
            console.log(e)
            this.cheatingData = e
            this.alertData = e[e.length -1]
            this.overlay = !this.overlay
        }
    }
}
</script>

<style scoped>

.row-1 {
}

.column-1 {
    background-color: aqua;
    overflow-y: scroll;
}

.column-2 {
    background-color: blue;
    overflow-y: scroll;
}

.column-3 {
    background-color: purple;
    overflow: hidden;
    align-items: center;
    justify-content: center;
}

</style>
