<template>
    <div style="max-width: 1080px; margin: 0 auto; padding: 10px;">
        
        <div class="container">LOGIN PAGE</div>

        <div id="user_formdata" class="container-fluid">

            <div class="row">   

                <div class="col-sm-12 col-md-12 col-xs-12 row">
                    <span class="col-sm-12 col-md-12 col-xs-12">e-mail: </span>
                    <input  type=text v-model.lazy="userData.userEmail" 
                            class="col-sm-12 col-md-12 col-xs-12">
                </div>

                <div class="col-sm-12 col-md-12 col-xs-12 row">
                    <span class="col-sm-12 col-md-12 col-xs-12">Password: </span>
                    <input  type=password v-model.lazy="userData.userPassword" 
                            class="col-sm-12 col-md-12 col-xs-12">
                </div>

            </div>

        </div>

        <div id="login_button">
            <button @click="submitLoginData()">LOGIN</button>
        </div>

    </div>
</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { bus } from '../../main'

export default {
    components: {

    },
    data() {
        return {
            registrationEndpoint: "http://localhost:3005/login_service",
            userData: {
                userEmail: "",
                userPassword: "",
                userName: ""
            }
        }
    },
    methods: {
        submitLoginData() {
            var valid = this.validateUserData()
            if (valid != true) {
                return
            }
            // define JSON struct
            var userDataJSON = {
                "user_email": this.userData.userEmail,
                "user_password": this.userData.userPassword
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
                    this.userData.userName = response.data.user_name
                    this.goToFaceVerification()       
                } else {
                    alert(response.data.return)
                    return
                }
             }).catch(error => {
                console.log(error)
                alert("LOGIN FAILED, PLEASE RETRY")
                })
        },
        validateUserData() {
            if (!this.userData.userEmail || !this.userData.userPassword) {
                alert("PLEASE FILL OUT ALL THE DATA")
                return false
            } else {
                return true
            }
        },
        goToFaceVerification() {
            this.$router.push({path:'/faceverification', query:{userEmail: this.userData.userEmail, userName: this.userData.userName}})
//	    this.$router.push({path:}) 
       }
    }
}

</script>

<style scoped>

.container {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>
