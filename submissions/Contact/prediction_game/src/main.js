// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import Vuex from 'vuex'
import VModal from 'vue-js-modal'
import store from './store'

import Content from './components/Content'
import Header from './components/Header.vue'

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(Vuex)
Vue.use(VModal, { dynamic: true, injectModalsContainer: true })
/* eslint-disable no-new */


new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})

new Vue({
  el: '#content',
  store,
  components: { Content },
  template: '<Content/>'
})

new Vue({
  el: '#header',
  store,
  components: {Header},
  template: '<Header/>'
})
