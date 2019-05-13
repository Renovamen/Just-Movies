import Vue from 'vue'
import App from './App'
import router from './router'
import VueAntd from 'ant-design-vue'
import '../static/reset.css'
import 'ant-design-vue/dist/antd.css'
import axios from 'axios'

Vue.config.productionTip = false
Vue.use(VueAntd)

Vue.prototype.$http = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
