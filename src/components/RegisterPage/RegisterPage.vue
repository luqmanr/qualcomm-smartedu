<template>
    <div class="container row" style="max-width: 1080px; margin: 0 auto; padding: 10px;">
        
        <!-- <div class="container-fluid col-md-12">

            <div></div>
            <div></div>
            
        </div> -->

        <div id="register_view" class="container-fluid col-md-12">

            <div class="row" style="max-width: 90vw; margin: auto;">
                <!-- <img :src="userData.userImage" style="max-height: 100%; max-width: 100%;"> -->
                <webcam class="col-md-6"></webcam>
            
                <div class="row col-md-6">   

                    <div class="col-sm-12 col-md-12 col-xs-12 row">
                        <span class="col-sm-12 col-md-12 col-xs-12">Nama: </span>
                        <input  type=text v-model.lazy="userData.userName"
                                class="col-sm-12 col-md-12 col-xs-12">
                    </div>

                    <div class="col-sm-12 col-md-12 col-xs-12 row">
                        <span class="col-sm-12 col-md-12 col-xs-12">e-mail: </span>
                        <input  type=email v-model.lazy="userData.userEmail"
                                class="col-sm-12 col-md-12 col-xs-12">
                    </div>

                    <div class="col-sm-12 col-md-12 col-xs-12 row" ref="password" :class="password_error.class">
                        <span class="col-sm-12 col-md-12 col-xs-12">Password: {{password_error.message}}</span>
                        <input  type=password v-model.lazy="userData.userPassword"
                                class="col-sm-12 col-md-12 col-xs-12">
                    </div>

                    <div class="col-sm-12 col-md-12 col-xs-12 row" ref="passwordReconfirmed" :class="password_error.class">
                        <span class="col-sm-12 col-md-12 col-xs-12">Re-confirm Password: {{password_error.message}}</span>
                        <input  type=password v-model.lazy="userData.userPasswordReconfirmed"
                                class="col-sm-12 col-md-12 col-xs-12">
                    </div>

                    <div class='col-sm-12 col-md-12 col-xs-12 row button'>
                        <label  class="col-sm-12 col-md-12 col-xs-12"
                                for="submit-userdata">REGISTRASI</label>
                        <input  @click="submitUserData()" 
                                id="submit-userdata" 
                                data-disable-touch-keyboard
                                readonly></input>
                    </div>

                </div>

            </div>

        </div>

        <!-- <div class="container-fluid">

            <div class="row container">
                <div id="submit_button" class="col-sm-12 container">
                    <button @click="submitUserData()">SUBMIT</button>
                </div>
                <div id="login_button" v-if="registrationStatus == true" class="col-sm-12">
                    <button @click="goToLoginPage()">GO TO LOGIN PAGE</button>
                </div>
            </div>
            
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
            registrationEndpoint: "http://localhost:3005/register_user",
            userData: {
                userName: null,
                userEmail: null,
                userPassword: null,
                userPasswordReconfirmed: null,
                userImage: null
            },
            registrationStatus: false,
            password_error: {
                status: false,
                message: "",
                class: "password-normal"
            },
            
        }
    },
    methods: {
        submitUserData() {
            var valid = this.validateUserData()
            if (valid != true) {
                return
            }
            if (this.password_error.status == false) {
                // define JSON struct
                var userDataJSON = {
                    "user_name": this.userData.userName,
                    "user_email": this.userData.userEmail,
                    "user_password": this.userData.userPassword,
                    "user_image": this.userData.userImage
                };  console.log(userDataJSON);
                // Endpoint location
                var apiEndpoint = this.registrationEndpoint
                // hit Endpoint with axios.post
                axios.post(apiEndpoint,
                JSON.stringify(userDataJSON),
                {headers :{'Content-Type': 'application/json'}},
                {timeout: 1000})
                .then((response) => {
                    console.log(response)
                    if (response.data.status == 200) {
                        this.registrationStatus = true  
                    } else {
                        alert("USER ALREADY EXISTS")
                        return
                    }
                }).catch(error => {
                    console.log(error)
                    alert("REGISTRATION FAILED, PLEASE TRY AGAIN")
                    })
            } else {
                alert("PASSWORD DOESN'T MATCH, PLEASE RE-ENTER YOUR PASSWORD")
            }
        },
        receiveSnapshotFromBus() {
            bus.$on('getSnapshot', (image) => { // ini fungsi yang menerima snapshot dari webcam
                // this.userData.userImage = image
                this.userData.userImage = image.split(',')[1]
                console.log("image captured")
            })
        },
        goToLoginPage() {
            this.$router.push('/login')
        },
        updatePasswordStatus() {
            var passwordEl = this.$refs["password"]
            var passwordReconfirmedEl = this.$refs["passwordReconfirmed"]

            if (this.userData.userPasswordReconfirmed != this.userData.userPassword) {
                this.password_error.message = "PASSWORD DOESN'T MATCH"
                this.password_error.class = "password-error"
                this.password_error.status = true
            } else {
                this.password_error.message = "PASSWORD MATCH"
                this.password_error.class = "password-true"
                this.password_error.status = false
            }
        },
        validateUserData() {
            if (!this.userData.userName || !this.userData.userEmail || !this.userData.userPassword || !this.userData.userImage) {
                alert("PLEASE FILL OUT ALL THE DATA")
                return false
            } else {
                return true
            }
        }
    },
    computed: {
        userPasswordReconfirmed() {
            return this.userData.userPasswordReconfirmed
        },
        userPassword() {
            return this.userData.userPassword
        }
    },
    watch: {
        userPasswordReconfirmed() {
            this.updatePasswordStatus()
        },
        userPassword() {
            this.updatePasswordStatus()
        }
    },
    created() {
        this.receiveSnapshotFromBus()
    }
}

</script>

<style scoped>

#register_view {
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
}

.password-true {
    color: green;
} .password-true input {
    color: green;
    border-color: green;
}

.password-warning {
    color: orange;
} .password-warning input {
    color: orange;
    border-color: orange;
}

.password-error {
    color: red;
} .password-error input {
    color: red;
    border-color: red;
}
/* 
#user_formdata {
    display: flex;
    align-items: center;
    justify-content: center;
} */

</style>