import Vue from 'vue'
import App from './App'
import router from './router'
import VueAntd from 'ant-design-vue'
import '../static/reset.css'
import 'ant-design-vue/dist/antd.css'

Vue.config.productionTip = false

Vue.use(VueAntd)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
