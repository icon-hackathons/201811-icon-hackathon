/* eslint-disable no-param-reassign */
import AT from './action-types';
import ServerAPI from '../api/ServerAPI';
import DpesProjectAPI from '../api/DpesProjectAPI';

/* mutation-types */
const GET_REVIEW_RESULT_LOADING = 'GET_REVIEW_RESULT_LOADING';
const GET_REVIEW_RESULT_SUCCESS = 'GET_REVIEW_RESULT_SUCCESS';

export default {
  state: {
    loading: true,
    reviewResult: [],
  },
  mutations: {
    [GET_REVIEW_RESULT_LOADING](state) {
      state.loading = true;
    },
    [GET_REVIEW_RESULT_SUCCESS](state, payload) {
      state.loading = false;
      state.reviewResult = payload;
    },
  },
  actions: {
    async [AT.AUDIT.GET_REVIEW_RESULT]({ commit }, {
      projectAddress,
    }) {
      commit(GET_REVIEW_RESULT_LOADING);
      const payload1 = await DpesProjectAPI.getReviewResult({
        projectAddress,
        userAddress: 'hxcacb3b4b04f0f0e4e1667163476d436c87dd11bc',
      });
      const payload2 = await DpesProjectAPI.getReviewResult({
        projectAddress,
        userAddress: 'hx72f7f531dcd26c6f34f691ec54c0ea9a255d2508',
      });
      commit(GET_REVIEW_RESULT_SUCCESS, [
        payload1,
        payload2,
      ]);
    },
  },
};
