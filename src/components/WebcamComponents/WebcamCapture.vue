<template>

    <div class="container-fluid">
        <!-- Stream video from webcam -->
        <div class="video-wrap row d-flex justify-content-center">
            <div class="testingcuy">
                <!-- videoDOM -->
                <video 
                    for="snapout" 
                    ref="video" 
                    playsinline autoplay class="video-image">
                </video>
            </div>
            
            <!-- HASIL WEBCAM SNAPSHOT-->
            <canvas ref="canvas" 
                    :width="videoMetaData.width" 
                    :height="videoMetaData.height"> <!-- set berapa ukuran image yang diinginkan -->
            </canvas>
        </div>
        <div class="controller row d-flex justify-content-center">

            <!-- button untuk snap picture -->
            <div class='col-sm-12 d-flex justify-content-center'>
                <label for="snapout" 
                    ref="snap">Capture</label>
                <input v-on:click="captureCanvas(); sendSnapshotToBus();" 
                    id="snapout" 
                    data-disable-touch-keyboard
                    readonly></input>
            </div>

            <div class='col-sm-12 d-flex justify-content-center'>
                <label for="switch-cam" 
                    ref="switch-cam">Switch Camera</label>
                <input v-on:click="switchCamera()" 
                    id="switch-cam" 
                    data-disable-touch-keyboard
                    readonly></input>
            </div>

            <div class='col-sm-12 d-flex justify-content-center'>
                <label for="stop-video" 
                    ref="stop-video">Stop Camera</label>
                <input v-on:click="stopVideo()" 
                    id="stop-video" 
                    data-disable-touch-keyboard
                    readonly></input>
            </div>

        </div>

    </div>
  
</template>
  
<script>

import { bus } from '../../main';

'use strict';

export default {
    components: {
        // QrcodeStream
    },
    data() {
        return {
            videoObject: undefined,
            constraints : {
                audio: false,
                video: {
                    width: {
                      min: 320, ideal: 1280, max: 1280 // setting resolusi rekaman video
                    },
                    height: {
                      min: 240, ideal: 720, max: 720 // setting resolusi rekaman video
                    },
                    frameRate: {
                      min: 5, ideal: 60, max: 60 // setting fps rekaman video
                    },
                    // facingMode: {
                    //     exact: 'user'
                    // }
                }
            },
            videoMetaData: {
                width: undefined,
                height: undefined
            },
            snapshot: [],
            videoStatus: false,
        }
    },
    methods: {
        getVideo() {
            try {
                navigator.mediaDevices.getUserMedia(this.constraints)
                  .then(mediaStream => {
                      const video = document.querySelector('video')
                      video.srcObject = mediaStream
                      this.videoObject = mediaStream
                      this.videoStatus = true;
                      
                      video.onloadedmetadata = (e) => {
                          video.play();
                          this.videoMetaData.width = e.srcElement.videoWidth
                          this.videoMetaData.height = e.srcElement.videoHeight
                      };

                      this.captureVideo(video)
                    });
            }
            catch(e) {
                console.error("no video")
            }
        },
        stopVideo() {
            this.videoObject.getTracks().forEach(track => track.stop())
            this.videoStatus = false
        },
        captureVideo(video) {
            const canvas = this.$refs.canvas
            const snap = this.$refs.snap
            var context = canvas.getContext('2d')
            // apply mirroring
            context.translate(canvas.width, 0)
            context.scale(-1, 1)

        },
        captureCanvas() {
            const video = document.querySelector('video')
            console.log(video)
            const canvas = this.$refs.canvas
            var context = canvas.getContext('2d')
            context.drawImage(video,0,0,this.videoMetaData.width,this.videoMetaData.height) // harus sesuai dengan ukuran canvasDOM

            this.snapshot = canvas.toDataURL()
        },
        switchCamera() {
            // console.log(this.constraints.video.facingMode.exact)
            if (this.constraints.video.facingMode.exact == "user") {
                this.constraints.video.facingMode.exact = "environment"
                this.stopVideo()
                this.getVideo()
            } else {
                this.constraints.video.facingMode.exact = "user"
                this.stopVideo()
                this.getVideo()
            }
        },
        sendSnapshotToBus() {
            console.log("snapshot sent")
            bus.$emit('getSnapshot', this.snapshot);
        },
        toggleWebcamFromBus() {
            bus.$on('toggleWebcam', (status) => {
                this.videoStatus = status
                if (status == false) {
                    this.stopVideo()
                }
                console.log(this.videoStatus)
            })
        }
    },
    mounted() {
        this.getVideo()
    },
    computed: {

    },
    created() {
        this.toggleWebcamFromBus()
    },
    watch: {
        qrString: function(e) {
            //do something when the data changes.
            if (e) {
                setTimeout(this.captureCanvas, 2500)
                setTimeout(this.sendSnapshotToBus, 2500)
            }
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

/* .testingcuy {
    height: 300px;
    width: 300px;
    margin: auto;
    align-items: center;
    align-self: center;
    overflow: hidden;
    background-color: black;
    display: flex;
    flex-wrap: wrap;
    align-content: center
} */

.video-image {
    transform: rotateY(180deg);
    -webkit-transform:rotateY(180deg); /* Safari and Chrome */
    -moz-transform:rotateY(180deg); /* Firefox */
}

.controller input{
    /* margin-left: 150px; */
    z-index: -2;
    opacity: 0;
    /* margin-left: 0px; */
}

.controller label{
    border-radius: 4px;
    background: dodgerblue;
    color: white;
    width: 15vh;
    cursor: pointer;
    margin: auto;
    align-items: center;
    align-self: center;
}

.video-wrap {
    height: 300px;
    width: 300px;
    overflow: hidden;
    margin: auto;
    align-items: center;
    align-self: center;
} .video-wrap video {
      z-index: 0;
      height: 300px;
      width: 400px;
      margin-left: -50px;
  }
  .video-wrap canvas {
      z-index: -1;
      height: 300px;
      width: 400px;
      margin-left: -50px;
  }

</style>
  