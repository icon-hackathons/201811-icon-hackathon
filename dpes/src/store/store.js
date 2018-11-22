import Vue from 'vue';
import Vuex from 'vuex';
import LoginForm from './LoginForm';
import ProfileForm from './ProfileForm';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    LoginForm,
    ProfileForm,
    // Evaluation: Evaluation,
  },
});
