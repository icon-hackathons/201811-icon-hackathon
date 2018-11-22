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
    [SUBMIT_SUCCESS](state) {
      state.isSuccess = true;
    },
    [RESET](state) {
      state.isSuccess = false;
    },
  },
  actions: {
    async [AT.PROFILE_FORM.SUBMIT]({ commit }, payload) {
      await ServerAPI.createProfile(payload);
      commit(SUBMIT_SUCCESS);
    },
    [AT.PROFILE_FORM.RESET]({ commit }) {
      commit(RESET);
    },
  },
};
