<template>
    <header>
        <h1>{{title}}</h1>
        <Button 
            v-show="homePage"
            @btn-click="$emit('btn-click')" 
            class="btn" 
            :text="showAddTask ? 'Close' : 'Add Task'" 
            :color="showAddTask ? 'red' : 'green'">
        </Button>
    </header>
</template>

<script>
import Button from './Button'
export default {
    name: 'Header-comp',
    props: {
        title: String,
        showAddTask: Boolean
    },
    components: {
        Button
    },
    computed: {
        homePage() {
            if(this.$route.path === '/') {
                return true
            } else {
                return false
            }
        }
    }
}
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center; 
        margin-bottom: 20px;
        border: 1px solid;
        padding: 5px
    }

    .btn {
        color: inline-block;
        background: black;
        color: #fff;
        border: none;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        font-size: 15px;
        font-family: inherit;
    }
</style>