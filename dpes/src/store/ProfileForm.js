/* eslint-disable no-param-reassign */
import AT from './action-types';
import ServerAPI from '../api/ServerAPI';

/* mutation-types */
const SUBMIT_SUCCESS = 'SUBMIT_SUCCESS';
const RESET = 'RESET';

export default {
  state: {
    isSuccess: false,
  },
  mutations: {
    [SUBMIT_SUCCESS](state, payload) {
      state.auth = true;
      state.userId = payload;
    },
    [RESET](state) {
      state.auth = false;
    },
  },
  actions: {
    async [AT.PROFILE_FORM.SUBMIT]({ commit }, payload) {
      const checkAuth = await ServerAPI.createProfile(payload.email, payload.pw);
      if (checkAuth) {
        commit(SUBMIT_SUCCESS);
      }
    },
    [AT.PROFILE_FORM.RESET]({ commit }) {
      commit(RESET);
    },
  },
};
