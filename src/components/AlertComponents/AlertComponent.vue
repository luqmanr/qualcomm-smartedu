<template>

    <div>
        <b-alert
          :show="dismissCountDown"
          dismissible
          variant="danger"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged"
          >
          <div style="background-color: red; color: white; padding: 5% 5% 5% 5%;">
            <p>{{alertMessage[1]}}</p>
            <p>Kecurangan Terdeteksi!!</p>
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
        }
    },
    data() {
        return {
            dismissSecs: 5,
            dismissCountDown: 0,
            alertMessage: this.alertData.split(",")
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

</style>