import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'


window.http = axios
new Vue({
  el: '#app',
  render: h => h(App),
  //挂载路由
  router
})
