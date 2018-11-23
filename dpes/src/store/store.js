import Vue from 'vue';
import Vuex from 'vuex';
import Profile from './Profile';
import LoginForm from './LoginForm';
import ProfileForm from './ProfileForm';
import EvaluationLogin from './EvaluationLogin';
import Evaluation from './Evaluation';
import Workspace from './Workspace';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    Profile,
    LoginForm,
    ProfileForm,
    EvaluationLogin,
    Evaluation,
    Workspace,
  },
});
