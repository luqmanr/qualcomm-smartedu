<template>
    <div style="max-width: 1080px; margin: 0 auto; padding: 10px;">
        
        <div>FACE VERIFICATION PAGE</div>

        <div id="user_formdata" class="container-fluid">

            <div class="row">
                <webcam class="col-sm-12 col-md-12 col-xs-12"></webcam>
            </div>

            <div class="row">   

                <!-- <div class="col-sm-12 col-md-12 col-xs-12 row">
                    <span class="col-sm-12 col-md-12 col-xs-12">Nama: </span>
                    <input  type=text v-model.lazy="userData.userName"
                            class="col-sm-12 col-md-12 col-xs-12">
                </div> -->

            </div>

        </div>

        <div id="submit_button">
            <button @click="submitUserData()">VERIFY FACE</button>
        </div>

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
            registrationEndpoint: "http://localhost:3005/face_verification",
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
            var apiEndpoint = this.registrationEndpoint
            // hit Endpoint with axios.post
            axios.post(apiEndpoint,
              JSON.stringify(userDataJSON),
              {headers :{'Content-Type': 'application/json'}},
              {timeout: 10})
            .then((response) => {
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
        goToExamPage() {
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
/* 
#user_formdata {
    display: flex;
    align-items: center;
    justify-content: center;
} */

</style>
