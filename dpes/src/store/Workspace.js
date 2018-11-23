/* eslint-disable no-param-reassign */
import { IconAmount } from 'icon-sdk-js';
import AT from './action-types';
import DpesScoreAPI from '../api/DpesScoreAPI';
import DpesProjectAPI from '../api/DpesProjectAPI';
import ServerAPI from '../api/ServerAPI';

/* mutation-types */
const GET_WORKSPACE_LOADING = 'GET_WORKSPACE_LOADING';
const GET_WORKSPACE_SUCCESS = 'GET_WORKSPACE_SUCCESS';

const DEPLOY_WORKSPACE_LOADING = 'DEPLOY_WORKSPACE_LOADING';
const DEPLOY_WORKSPACE_SUCCESS = 'DEPLOY_WORKSPACE_SUCCESS';

export default {
  state: {
    loading: false,
    workspace: {},
    newWorkspaceAddress: '',
  },
  mutations: {
    [GET_WORKSPACE_LOADING](state) {
      state.loading = true;
    },
    [GET_WORKSPACE_SUCCESS](state, payload) {
      state.loading = false;
      state.workspace = Object.assign({}, state.workspace, {
        projectName: payload.name,
        dueDate: parseInt(payload.due_date, 16) - ((new Date()).getTime() * 1000),
        prizeAmount: Number(IconAmount.of(payload.prize_amount, IconAmount.Unit.LOOP).convertUnit(IconAmount.Unit.ICX).value),
        projectAddress: payload.projectAddress,
      });
    },
    [DEPLOY_WORKSPACE_LOADING](state) {
      state.loading = true;
    },
    [DEPLOY_WORKSPACE_SUCCESS](state, payload) {
      state.loading = false;
      state.newWorkspaceAddress = payload;
    },
  },
  actions: {
    async [AT.WORKSPACE.GET_WORKSPACE]({ commit }, payload) {
      commit(GET_WORKSPACE_LOADING);
      const workspaceData = await DpesProjectAPI.getProjectInfo(payload);
      console.log(workspaceData);
      commit(GET_WORKSPACE_SUCCESS, {
        ...workspaceData,
        projectAddress: payload,
      });
    },
    async [AT.WORKSPACE.DEPLOY_WORKSPACE]({ commit }, payload) {
      commit(DEPLOY_WORKSPACE_LOADING);
      const tx = await DpesProjectAPI.createProject(payload);
      const address = await DpesScoreAPI.checkTransaction(tx, true);
      if (address) {
        await ServerAPI.createWorkspace(address);
        commit(DEPLOY_WORKSPACE_SUCCESS, address);
      }
    },
  },
};
