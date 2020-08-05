<template>
    <div class="container row" style="max-width: 1080px; margin: 0 auto; padding: 10px;">
        
        <!-- <div class="container-fluid col-md-12">

            <div></div>
            <div></div>
            
        </div> -->

        <div id="login_view" class="container-fluid col-md-12">

            <div class="row" style="margin: auto;">   

                <div class="col-sm-12 col-md-12 col-xs-12 row">
                    <span class="col-sm-12 col-md-12 col-xs-12">e-mail: </span>
                    <input  type=email v-model.lazy="userData.userEmail" 
                            class="col-sm-12 col-md-12 col-xs-12">
                </div>

                <div class="col-sm-12 col-md-12 col-xs-12 row">
                    <span class="col-sm-12 col-md-12 col-xs-12">Password: </span>
                    <input  type=password v-model.lazy="userData.userPassword" 
                            class="col-sm-12 col-md-12 col-xs-12">
                </div>

                <div class='col-sm-12 col-md-12 col-xs-12 row button'>
                    <label  class="col-sm-12 col-md-12 col-xs-12"
                            for="submit-userdata">LOGIN</label>
                    <input  @click="submitLoginData()" 
                            id="submit-userdata" 
                            data-disable-touch-keyboard
                            readonly></input>
                </div>

            </div>

        </div>

        <!-- <div id="login_button">
            <button @click="submitLoginData()">LOGIN</button>
        </div> -->


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
                userPassword: ""
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
                console.log(response)
                if (response.data.status == 200) {
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
            this.$router.push({path:'/faceverification', query:{userEmail: this.userData.userEmail}})
        }
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