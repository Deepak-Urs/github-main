<template>
  <div class="container">
    <Header title="Task Tracker"></Header>
    <AddTask @add-task="addTask"/>
    <Tasks @toggle-reminder="toggleReminder" @delete-task="deleteTask" :tasks="tasks"></Tasks>
  </div>
  
  <!--<img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
</template>

<script>
import Tasks from './components/Tasks.vue'
import Header from './components/Header.vue'
import AddTask from './components/AddTask.vue'

export default {
  name: "App",
  components: {
    Header,
    Tasks,
    AddTask
  },
  data() {
    return {
      tasks: []
    }
  },
  methods: {
    addTask(task) {
      this.tasks = [...this.tasks, task]
    },
    deleteTask(id) {
      if(confirm('Are you sure?')) {
        this.tasks = this.tasks.filter((task) => task.id !== id)
      }
    },
    toggleReminder(id) {
      console.log('id seen', id);
      this.tasks = this.tasks.map((task) => task.id === id ? { ...task, reminder: !task.reminder} : task)
    }
  },
  created() {
    this.tasks = [
      {
        id: 1,
        text: 'Doctor appointement',
        day: 'March 1st at 2:30pm',
        reminder: true
      },
      {
        id: 2,
        text: 'Meeting at school',
        day: 'March 2nd at 2:30pm',
        reminder: true
      },
      {
        id: 3,
        text: 'Food Shopping',
        day: 'March 3rd at 2:30pm',
        reminder: false
      },
    ]
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
