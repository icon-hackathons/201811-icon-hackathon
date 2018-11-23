/* eslint-disable no-param-reassign */
import AT from './action-types';
import ServerAPI from '../api/ServerAPI';
import DpesProjectAPI from '../api/DpesProjectAPI';

/* mutation-types */
const GET_REVIEW_RESULT_LOADING = 'GET_REVIEW_RESULT_LOADING';
const GET_REVIEW_RESULT_SUCCESS = 'GET_REVIEW_RESULT_SUCCESS';

export default {
  state: {
    loading: false,
  },
  mutations: {
    [GET_REVIEW_RESULT_LOADING](state) {
      state.loading = true;
    },
    [GET_REVIEW_RESULT_SUCCESS](state) {
      state.loading = false;
    },
  },
  actions: {
    // async [AT.AUDIT.GET_REVIEW_RESULT]({ commit }, {
    //     projectAddress,
    //     userAddress
    // }) {
    //   await DpesProjectAPI.getReviewResult({
    //     projectAddress,
    //     userAddress
    //   });
    //   commit(GET_REVIEW_RESULT_SUCCESS);
    // },
  },
};
