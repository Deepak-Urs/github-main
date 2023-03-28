<template>
    <div @dblclick="$emit('toggle-reminder', task.id)" :class="[task.reminder ? 'reminder' : '', 'task']">
        <div class="row-1">
            <h3>{{ task.text }}</h3>
            <i @click="$emit('delete-task', task.id)" class="fas fa-times"></i>
        </div>
        <div class="row-2">
            <p>{{ task.day }}</p>
        </div>
    </div>
    
</template>

<script>
export default {
   name: 'Task-comp',
   props: {
    task: Object
   }
}
</script>

<style scoped>
    .task {
        background: #f4f4f4;
        margin: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }

    .row-1 {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .row-2 {
        display: flex;
    }

    .task.reminder {
        border-left: 5px solid green;
    }

    .task h3 {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .fas {
        color: red;
    }
</style>