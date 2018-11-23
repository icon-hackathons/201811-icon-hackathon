import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:3000',
});

const getProfile = async (id) => {
  const profile = await api.get(`/profiles?id=${id}`);
  return profile.data;
};

const createProfile = async ({
  firstName,
  lastName,
  img,
  walletAddress,
  company,
  team,
  position,
  selfReview,
  userId,
} = {}) => {
  const res = await api.post('/profiles', {
    name: `${firstName} ${lastName}`,
    img,
    walletAddress,
    company,
    team,
    position,
    selfReview,
    userId,
  });
  return res.data;
};

const createUser = async (email, pw) => {
  const res = await api.post('/users', {
    email,
    pw,
  });
  return res.data;
};

const createWorkspace = async (address) => {
  const res = await api.post('/workspaces', {
    address,
  });
  return res.data;
};

const checkAuth = async (email, pw) => {
  const users = await api.get('/users');
  const user = users.data.filter(item => item.email === email && item.pw === pw);
  const result = user.length > 0 ? user[0].id : false;
  return result;
};

const getWorkspaceList = async () => {
  const workspaces = await api.get('/workspaces');
  const addressMap = workspaces.data.map(workspace => workspace.address)
  return addressMap;
};

const getGroupList = async () => {
  const groups = await api.get('/groups');
  return groups;
};

const getProfileList = async () => {
  const users = await api.get('/profiles?groupId=1');
  return users;
};

export default {
  getProfile,
  createProfile,
  createUser,
  createWorkspace,
  checkAuth,
  getWorkspaceList,
  getGroupList,
  getProfileList,
};
