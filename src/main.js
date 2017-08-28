import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

// 添加这行代码后，在 App.vue 及及其他组件中就不用导入 `axios` 了，可以直接用
// http.get(...), http.post(...) ...
window.http = axios

new Vue({
  el: '#app',
  render: h => h(App)
})