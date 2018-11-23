/* eslint-disable no-param-reassign */
import AT from './action-types';
import IconexConnectAPI from '../api/IconexConnectAPI';
import DpesScoreAPI from '../api/DpesScoreAPI';
import Builder from '../sdk/Builder';
import Constants from '../constants';

/* mutation-types */
const PARENT_LOG_IN_SUCCESS = 'PARENT_LOG_IN_SUCCESS';
const CHILD_LOG_IN_SUCCESS = 'CHILD_LOG_IN_SUCCESS';
const WALLET_LOG_OUT_SUCCESS = 'WALLET_LOG_OUT_SUCCESS';
const WALLET_SIGN_UP_SUCCESS = 'WALLET_SIGN_UP_SUCCESS';
const WALLET_SIGN_UP_FAIL = 'WALLET_SIGN_UP_FAIL';
const LOADING = 'LOADING';
const RESET = 'RESET';

export default {
  state: {
    loading: false,
    parent: {
      parentAddress: '',
      parentLevel: 0,
    },
    child: {
      childAddress: '',
      childLevel: 0,
    },
  },
  mutations: {
    [LOADING](state) {
      state.loading = true;
    },
    [PARENT_LOG_IN_SUCCESS](state, payload) {
      state.parent = Object.assign({}, state.parent, payload);
    },
    [CHILD_LOG_IN_SUCCESS](state, payload) {
      state.parent = {};
      state.child = Object.assign({}, state.child, payload);
    },
    [WALLET_SIGN_UP_SUCCESS](state, payload) {
      state.loading = false;
      state.parent = {};
      state.child = Object.assign({}, state.child, payload);
    },
    [WALLET_SIGN_UP_FAIL](state) {
      state.loading = false;
    },
    [RESET](state) {
      state.parent = {};
      state.child = {};
    },
  },
  actions: {
    async [AT.EVALUATION_LOGIN.PARENT_LOG_IN]({ commit }) {
      const parentAddress = await IconexConnectAPI.getAddress();
      const checkParentExist = await DpesScoreAPI.checkParentExist(parentAddress);
      if (!parseInt(checkParentExist, 16)) {
        alert('parent not exist');
      } else {
        const parentLevel = await DpesScoreAPI.getParentLevel(parentAddress);
        commit(PARENT_LOG_IN_SUCCESS, {
          parentLevel: parseInt(parentLevel, 16),
          parentAddress,
        });
      }
    },

    async [AT.EVALUATION_LOGIN.CHILD_LOG_IN]({ commit }) {
      const childAddress = await IconexConnectAPI.getAddress();
      const checkChildExist = await DpesScoreAPI.checkChildExist(childAddress);
      if (!parseInt(checkChildExist, 16)) {
        alert('child not exist');
      } else {
        const childLevel = await DpesScoreAPI.getChildLevel(childAddress);
        commit(CHILD_LOG_IN_SUCCESS, {
          childLevel: parseInt(childLevel, 16),
          childAddress,
        });
      }
    },

    async [AT.EVALUATION_LOGIN.SIGN_UP]({ commit }, {
      parentAddress,
      childAddress,
      isLeader,
    }) {
      commit(LOADING);
      const params = Builder.sendTx({
        from: parentAddress,
        to: Constants.DPES_SCORE_ADDRESS,
        stepLimit: '0xdbba0',
        networkId: '0x3',
        nonce: '0x1',
        value: '0x0',
        methodName: 'sign_up',
        params: {
          _child_address: childAddress,
          _is_leader: isLeader,
        },
      });
      const tx = await IconexConnectAPI.sendTransaction(params);
      const result = await DpesScoreAPI.checkTransaction(tx);
      if (result) {
        const childLevel = await DpesScoreAPI.getChildLevel(childAddress);
        commit(WALLET_SIGN_UP_SUCCESS, {
          childAddress,
          childLevel: parseInt(childLevel, 16),
        });
      } else {
        commit(WALLET_SIGN_UP_FAIL);
      }
    },

    [AT.EVALUATION_LOGIN.LOG_OUT]({ commit }) {
      commit(WALLET_LOG_OUT_SUCCESS);
    },

    [AT.EVALUATION_LOGIN.RESET]({ commit }) {
      commit(RESET);
    },
  },
};
