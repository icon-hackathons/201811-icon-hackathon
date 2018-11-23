import Constants from '../constants';
import iconService from '../sdk/IconService';
import Builder from '../sdk/Builder';
import IconexConnectAPI from '../api/IconexConnectAPI';
import DpesScoreAPI from '../api/DpesScoreAPI';

const checkChildExist = async (childAddress) => {
  const call = Builder.call({
    to: Constants.DPES_SCORE_ADDRESS,
    methodName: 'check_child_exist',
    params: {
      _child_address: childAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const checkParentExist = async (parentAddress) => {
  const call = Builder.call({
    to: Constants.DPES_SCORE_ADDRESS,
    methodName: 'check_parent_exist',
    params: {
      _parent_address: parentAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const getChildLevel = async (childAddress) => {
  const call = Builder.call({
    to: Constants.DPES_SCORE_ADDRESS,
    methodName: 'get_child_level',
    params: {
      _child_address: childAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const getParentLevel = async (parentAddress) => {
  const call = Builder.call({
    to: Constants.DPES_SCORE_ADDRESS,
    methodName: 'get_parent_level',
    params: {
      _parent_address: parentAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const getTeamCount = async () => {
  const call = Builder.call({
    to: Constants.DPES_SCORE_ADDRESS,
    methodName: 'get_team_count',
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const getUserInfo = async (userAddress) => {
  const call = Builder.call({
    to: Constants.DPES_SCORE_ADDRESS,
    methodName: 'get_user_info',
    params: {
      _user_address: userAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const auditVote = async ({
  projectAddress,
  childAddress,
}) => {
  const params = Builder.sendTx({
    from: childAddress,
    to: Constants.DPES_SCORE_ADDRESS,
    stepLimit: '0xdbba0',
    networkId: '0x3',
    nonce: '0x1',
    value: '0x0',
    methodName: 'audit_vote',
    params: {
      _project_address: projectAddress,
    },
  });
  const tx = await IconexConnectAPI.sendTransaction(params);
  const result = await DpesScoreAPI.checkTransaction(tx);
  if (result) {
    return true;
  }
};

const checkTransaction = (param, isDeploy = false) => new Promise((resolve) => {
  let timer;
  const checkTx = (tx) => {
    const transactionResult = iconService.getTransactionResult(tx).execute();
    const flag = isDeploy ? transactionResult['scoreAddress'] : transactionResult['status'];
    if (flag) {
      clearInterval(timer);
      resolve(isDeploy ? flag : true);
    } else {
      clearInterval(timer);
      alert(transactionResult.failure.message);
      resolve(false);
    }
  };
  timer = setInterval(() => {
    checkTx(param);
  }, 1600);
});



export default {
  checkChildExist,
  checkParentExist,
  getChildLevel,
  getParentLevel,
  getTeamCount,
  getUserInfo,
  checkTransaction,
  auditVote,
};
