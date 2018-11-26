import {
  IconConverter,
  IconBuilder,
} from 'icon-sdk-js';
import Constants from '../constants';

const {
  CallBuilder,
  CallTransactionBuilder,
  DeployTransactionBuilder,
} = IconBuilder;

const call = ({
  methodName,
  params = {},
  to,
} = {}) => {
  const callBuilder = new CallBuilder();
  const obj = callBuilder
    .to(to)
    .method(methodName)
    .params(params)
    .build();
  return obj;
};

const sendTx = ({
  networkId,
  from,
  to,
  stepLimit,
  methodName,
  value,
  nonce,
  params = {},
} = {}) => {
  const callTransactionBuilder = new CallTransactionBuilder();
  const obj = callTransactionBuilder
    .nid(networkId)
    .from(from)
    .to(to)
    .nonce(nonce)
    .stepLimit(stepLimit)
    .value(value)
    .timestamp(`0x${((new Date()).getTime() * 1000).toString(16)}`)
    .method(methodName)
    .params(params)
    .version('0x3')
    .build();

  return {
    jsonrpc: '2.0',
    method: 'icx_sendTransaction',
    params: obj,
    id: 1,
  };
};


const deploy = ({
  networkId,
  from,
  stepLimit,
  content,
  params = {},
} = {}) => {
  const deployTransactionBuilder = new DeployTransactionBuilder();
  const obj = deployTransactionBuilder
    .nid(networkId)
    .from(from)
    .to(Constants.SCORE_INSTALL_ADDRESS)
    .stepLimit(stepLimit)
    .timestamp(`0x${((new Date()).getTime() * 1000).toString(16)}`)
    .contentType('application/zip')
    .content(`0x${content}`)
    .params(params)
    .version('0x3')
    .build();

  return {
    jsonrpc: '2.0',
    method: 'icx_sendTransaction',
    params: obj,
    id: 1,
  };
};

export default {
  call,
  sendTx,
  deploy,
};
