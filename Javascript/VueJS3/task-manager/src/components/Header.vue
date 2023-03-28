<template>
    <header>
        <h1>{{title}}</h1>
        <Button class="btn" text="Add Task" color="green"></Button>
    </header>
</template>

<script>
import Button from './Button'
export default {
    name: 'Header-comp',
    props: {
        title: String
    },
    components: {
        Button
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