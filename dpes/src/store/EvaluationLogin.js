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
const RESET = 'RESET';

export default {
  state: {
    auth: false,
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
    [PARENT_LOG_IN_SUCCESS](state, payload) {
      state.auth = true;
      state.parent = Object.assign({}, state.parent, payload);
    },
    [CHILD_LOG_IN_SUCCESS](state, payload) {
      state.auth = true;
      state.child = Object.assign({}, state.child, payload);
    },
    [RESET](state) {
      state.auth = false;
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
    async [AT.EVALUATION_LOGIN.SIGN_UP]({ commit }, {
      parentAddress,
      childAddress,
      isLeader,
    }) {
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
      console.log(params);
      const tx = await IconexConnectAPI.sendTransaction(params);
      console.log(tx);
    },
    async [AT.EVALUATION_LOGIN.CHILD_LOG_IN]({ commit }) {
      const childAddress = await IconexConnectAPI.getAddress();
      const checkChildExist = await DpesScoreAPI.checkChildExist(childAddress);
      if (!checkChildExist) {
        alert('child not exist');
      } else {
        const childLevel = await DpesScoreAPI.getChildLevel(childAddress);
        commit(WALLET_SIGN_UP_SUCCESS, {
          parentLevel: parseInt(childLevel, 16),
          childAddress,
        });
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
