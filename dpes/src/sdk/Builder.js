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
  params = {},
} = {}) => {
  const callTransactionBuilder = new CallTransactionBuilder();
  const obj = callTransactionBuilder
    .nid(networkId)
    .from(from)
    .to(to)
    .stepLimit(stepLimit)
    .timestamp((new Date()).getTime() * 1000)
    .method(methodName)
    .params(params)
    .version(IconConverter.toBigNumber(3))
    .build();
  return obj;
};

export default {
  call,
  sendTx,
};
