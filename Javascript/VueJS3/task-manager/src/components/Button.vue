<template>
    <button :style="{background: color}" class="">{{text}}</button>
</template>

<script>
export default {
    name: 'Button-comp',
    props: {
        text: String,
        color: String
    }
}
</script>