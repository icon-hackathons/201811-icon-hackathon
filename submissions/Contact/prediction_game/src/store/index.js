import Vue from 'vue'
import Vuex from 'vuex'
import questions from './modules/questions'
import account from './modules/account'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    questions,
    account
  }
})
