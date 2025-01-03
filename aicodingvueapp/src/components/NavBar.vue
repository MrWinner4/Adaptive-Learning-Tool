<template>
    <nav class = "navbar">
        <ul>
            <li><router-link to = "/dashboard">Dashboard</router-link></li>
            <li><router-link to = "/settings">Settings</router-link></li>
        </ul>
        <button @click="logout">Logout</button>
    </nav>
</template>

<script>
    export default {
        methods: {
            logout() {
                //LOGOUT LOGIC
                console.log("logging out");
            },
        },
    };
</script>

<style>
    .button {
        margin-left: auto;
        background-color: rgb(26, 26, 26);
        color: white;
        border-radius: 20px;
        padding: .5rem 1rem;
        cursor: pointer;
    } 
    .button:hover {
        background-color: rgb(0, 170, 255);
    }
    .navbar {
        position: sticky;
        top: 0;
        display: flex;
        margin: 0;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 0;
        background-color: rgb(26, 26, 26);
        color: white;
        widows: 100%;
        box-sizing: border-box;
    }
    .navbar ul {
        list-style: none;
        display: flex;
        gap: 15px;
    }
    body {
        margin: 0;
    }
    .navbar ul li {
        display: inline;
    }
    .navbar ul li a {
        color: white;
        text-decoration: none;
    }
    button {
        background: none;
        border: none;
        color: white;
        cursor: pointer;
    }

</style>