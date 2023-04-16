<template>
  <div class="container">
    <Header
      @btn-click="toggleAddTaskBtn"
      title="Task Tracker"
      :showAddTask="showAddTask"
    >
    </Header>

    <router-view :showAddTask="showAddTask"></router-view>
    <Footer></Footer>
  </div>

  <!--<img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
</template>

<script>

import Header from "./components/Header";
import Footer from "./components/Footer";


export default {
  name: "App",
  components: {
    Header,
    Footer
  },
  data() {
    return {
      showAddTask: false,
    };
  },
  methods: {
    toggleAddTaskBtn() {
      this.showAddTask = !this.showAddTask;
    }
  },
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
