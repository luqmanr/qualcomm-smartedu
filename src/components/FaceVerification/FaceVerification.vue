<template>
    <div style="max-width: 1080px; margin: 0 auto; padding: 10px;">
        
        <!-- <div class="container-fluid col-md-12">

            <div></div>
            <div></div>
            
        </div> -->

        <div id="login_view" class="container-fluid">

            <div class="row" style="max-width: 50vw; margin: auto;">
                <webcam class="col-md-6"></webcam>
                <!-- <div class="row">   
                    <div class="col-sm-12 col-md-12 col-xs-12 row">
                        <span class="col-sm-12 col-md-12 col-xs-12">Nama: </span>
                        <input  type=text v-model.lazy="userData.userName"
                                class="col-sm-12 col-md-12 col-xs-12">
                    </div>
                </div> -->
                <div class="row col-md-12">   
                    <div class='col-sm-12 col-md-12 col-xs-12 row button'>
                        <label  class="col-sm-12 col-md-12 col-xs-12"
                                for="submit-userdata">Verifikasi Muka</label>
                        <input  @click="submitUserData()" 
                                id="submit-userdata" 
                                data-disable-touch-keyboard
                                readonly></input>
                    </div>
                </div>

            </div>

        </div>

        <!-- <div id="submit_button">
            <button @click="submitUserData()">VERIFY FACE</button>
        </div> -->

    </div>
</template>

<script>
import Webcam from '../WebcamComponents/WebcamStreamCapture.vue'

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { bus } from '../../main'

export default {
    components: {
        "webcam": Webcam
    },
    data() {
        return {
            faceVerificationEndpoint: "http://localhost:3005/face_verification",
            cheatingMonitoringEndpoint: "http://localhost:3005/start_monitoring",
            userData: {
                userEmail: "",
                userImage: "",
		        userName: ""
            }
        }
    },
    methods: {
        submitUserData() {
            // define JSON struct
            var userDataJSON = {
                "user_email": this.userData.userEmail,
                "user_image": this.userData.userImage,
                "user_name": this.userData.userName
            };  console.log(userDataJSON);
            // Endpoint location
            var apiEndpoint = this.faceVerificationEndpoint
            // hit Endpoint with axios.post
            axios.post(apiEndpoint,
              JSON.stringify(userDataJSON),
              {headers :{'Content-Type': 'application/json'}},
              {timeout: 1000})
            .then(response => {
                console.log(response)
                if (response.data.status == 200) {
                    alert(response.data.return)
                    this.goToExamPage()   
                } else {
                    alert(response.data.return)
                    return
                }     
             }).catch(error => {
                console.log(error)
                alert("PLEASE RETAKE YOUR PHOTO")
                })
        },
        receiveSnapshotFromBus() {
            bus.$on('getSnapshot', (image) => { // ini fungsi yang menerima snapshot dari webcam
                // this.userData.userImage = image
                this.userData.userImage = image.split(',')[1]
                console.log("image captured")
                // console.log(this.userData.userImage)
            })
        },
        startCheatingMonitoring() {
            // this.stopAutoTrain()
            axios.post(
                this.cheatingMonitoringEndpoint,
                {timeout: 1000})
              .then(response => {
                  console.log(response)
              }).catch(error => {
                  console.log(error)
              })
        },
        stopAutoTrain() {
            axios.post(
                "http://localhost:3005/stop_autotrain",
                {timeout: 3000}
              ).then(response => {
                  console.log(response)
              }).catch(error => {
                  console.log(error)
              })
        },
        goToExamPage() {
            this.startCheatingMonitoring()
            this.$router.push('/exam')
        }
    },
    created() {
        this.userData.userEmail = this.$route.query.userEmail
        this.userData.userName = this.$route.query.userName
        console.log(this.userData)
        this.receiveSnapshotFromBus()
    }
}

</script>

<style scoped>

#login_view {
    padding: 5vh;
    max-width: 80vw;
    /* background-color:aliceblue; */
    border-radius: 1vh;
    border-style: outset;
    border-color:rgb(136, 169, 231)
}

.button {
    padding: 1vh;
} .button input{
    z-index: -2;
    opacity: 0;
    position: absolute;
} .button label{
    border-radius: 4px;
    background:green;
    color: white;
    font-weight: bolder;
    max-width: 25vh;
    cursor: pointer;
    margin: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 5vw;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto;
    max-height: 90vh;
}

</style>
