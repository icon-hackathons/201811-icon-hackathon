/* eslint-disable no-param-reassign */
import AT from './action-types';
import DpesScoreAPI from '../api/DpesScoreAPI';
import IconexConnectAPI from '../api/IconexConnectAPI';
import Builder from '../sdk/Builder';
import Constants from '@/constants';

/* mutation-types */
const VOTE_SUCCESS = 'VOTE';
const LOADING = 'LOADING';

export default {
  state: {
    loading: false,
  },
  mutations: {
    [LOADING](state) {
      state.loading = true;
    },
    [VOTE_SUCCESS](state) {
      state.loading = false;
    },
  },
  actions: {
    async [AT.EVALUATION.VOTE]({ commit }, {
      childAddress,
      userAddress,
      projectAddress,
      formattedJson,
    }) {
      commit(LOADING);
      const params = Builder.sendTx({
        from: childAddress,
        to: projectAddress,
        stepLimit: '0xdbba0',
        networkId: '0x3',
        nonce: '0x1',
        value: '0x0',
        methodName: 'vote',
        params: {
          _from: childAddress,
          _to: userAddress,
          _formatted_json: formattedJson,
          _message: '평소에 열심히 하는 분이라고 생각합니다.',
        },
      });
      const tx = await IconexConnectAPI.sendTransaction(params);
      const result = await DpesScoreAPI.checkTransaction(tx);
      if (result) {
        commit(VOTE_SUCCESS);
        alert('평가가 완료되었습니다.');
      }
    },
  },
};
