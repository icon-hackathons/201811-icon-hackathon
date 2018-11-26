/* eslint-disable no-param-reassign */
import AT from './action-types';
import DpesScoreAPI from '../api/DpesScoreAPI';
import ServerAPI from '../api/ServerAPI';

/* mutation-types */
const GET_PROFILE_LOADING = 'GET_PROFILE_LOADING';
const GET_PROFILE_SUCCESS = 'GET_PROFILE_SUCCESS';
const RESET = 'RESET';

export default {
  state: {
    loading: false,
    profile: {},
  },
  mutations: {
    [GET_PROFILE_LOADING](state) {
      state.loading = true;
    },
    [GET_PROFILE_SUCCESS](state, payload) {
      state.loading = false;
      state.profile = payload;
    },
    [RESET](state) {
      state.loading = false;
      state.profile = {};
    },
  },
  actions: {
    async [AT.PROFILE.GET_PROFILE]({ commit }, payload) {
      commit(GET_PROFILE_LOADING);
      const serverData = await ServerAPI.getProfile(payload);
      const contractData = await DpesScoreAPI.getUserInfo(serverData[0].walletAddress);
      const data = Object.assign({}, contractData, serverData[0]);
      commit(GET_PROFILE_SUCCESS, data);
    },
    [AT.PROFILE.RESET]({ commit }) {
      commit(RESET);
    },
  },
};
