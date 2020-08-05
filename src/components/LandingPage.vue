<template>
    <div>

        <div class="container row">
            <img :src="logoITB" max-height="50%" width="50%" style="padding: 10%;">
            <div class="container col-md-12" style="font-weight: bolder;">Selamat Datang di SmartEdu App</div>
        </div>
        
    </div>
</template>

<script>

import logoITB from '../assets/logo-ITB.png'

export default {
    components: {

    },
    data() {
        return {
            logoITB: logoITB
        }
    }
}

</script>

<style scoped>
    
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto;
    max-height: 90vh;
}

</style>