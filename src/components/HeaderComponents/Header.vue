<template>
    <div class="main-header">
        <router-link to="/" tag="button" exact>Halaman Utama</router-link>
        <router-link to="/login" tag="button" exact>Login</router-link>
        <router-link to="/register" tag="button" exact>Registrasi</router-link>
        <router-link to="/faceverification" tag="button" exact>To faceverification Page</router-link>
        <router-link to="/exam" tag="button" exact>To exam Page</router-link>
    </div>
</template>

<script>

</script>

<style scoped>

button {
    /* padding: 1vh; */
    min-width: 15vw;
    margin: auto;
    font-weight: bold;
}

.main-header {
    /* margin-top: 2vh; */
    padding: 1vh;
    background-color: rgb(99, 181, 236);
    border-style: outset;
    border-color: darkblue;
}

</style>