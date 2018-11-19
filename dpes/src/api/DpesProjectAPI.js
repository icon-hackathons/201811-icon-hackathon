import iconService from '../sdk/IconService';
import Builder from '../sdk/Builder';

const getMessageList = async (projectAddress, userAddress) => {
  const call = Builder.call({
    to: projectAddress,
    methodName: 'get_message_list',
    params: {
      _user_address: userAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const getReviewResult = async (projectAddress, userAddress) => {
  const call = Builder.call({
    to: projectAddress,
    methodName: 'get_review_result',
    params: {
      _user_address: userAddress,
    },
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

const getProjectInfo = async (projectAddress) => {
  const call = Builder.call({
    to: projectAddress,
    methodName: 'get_project_info',
  });
  const result = await iconService.call(call).execute(true);
  return result;
};

export default {
  getMessageList,
  getReviewResult,
  getProjectInfo,
};
