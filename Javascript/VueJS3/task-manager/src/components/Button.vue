<template>
    <button @click="onClick()" :style="{background: color}" class="">{{text}}</button>
</template>

<script>
export default {
    name: 'Button-comp',
    props: {
        text: String,
        color: String
    },
    methods: {
        onClick() {
            console.log('log happened')
        }
    }
}
</script>