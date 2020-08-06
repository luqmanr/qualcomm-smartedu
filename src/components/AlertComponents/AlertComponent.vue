<template>

    <div>
        <b-alert
          :show="dismissCountDown"
          :variant="buttonVariant"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged">
          <div :class="buttonClass">
            <p>{{alertData}}</p>
            <!-- <p>Kecurangan Terdeteksi!!</p> -->
            <p v-if="dismissSecs != 5">{{dismissCountDown}}</p>
          </div>
            
            <!-- <p>DI SINI NANTI ADALAH PLACEHOLDER CHEATING INFO</p>
            <p>Dismissing in {{ dismissCountDown }} seconds...</p> -->
        </b-alert>
        <!-- <b-button @click="showAlert" variant="info" class="m-1">
            Show alert with count-down timer
        </b-button> -->
    </div>

</template>

<script>
import { bus } from '../../main';

export default {
    components: {

    },
    props: {
        alertData: {
            default: "undefined"
        },
        dismissSecs: {
            default: 5
        },
        buttonVariant: {
            default: "danger"
        },
        buttonClass: {
            default: "countdown"
        }
    },
    data() {
        return {
            dismissCountDown: 0,
            // alertMessage: this.alertData.split(",")
            // alertData: {
            //     message: undefined,
            // }
        }
    },
    methods: {
        countDownChanged(dismissCountDown) {
            this.dismissCountDown = dismissCountDown
            if (dismissCountDown == 0) {
                this.emitOverlay()
            }
        },
        showAlert() {
            this.dismissCountDown = this.dismissSecs
        },
        emitOverlay() {
            this.$emit("emitOverlay")
        },
        receiveAlertMessage() {
            
        }
    },
    created() {
        this.showAlert()
    }
}
</script>

<style scoped>
.primary {
    
}
.warning {

}
.danger {
    background-color: red; color: white; 
}
.transparent {
    font-size: 200%;
    color: rgb(255, 57, 57);
    font-weight: bold;
    text-shadow: -1px -1px 0 rgb(167, 4, 4), 1px -1px 0 rgb(167, 4, 4), -1px 1px 0 rgb(167, 4, 4), 1px 1px 0 rgb(167, 4, 4);
}
</style>
