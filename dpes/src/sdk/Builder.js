import {
  IconConverter,
  IconBuilder,
} from 'icon-sdk-js';
import Constants from '../constants';

const {
  CallBuilder,
  CallTransactionBuilder,
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

export default {
  call,
  sendTx,
};
